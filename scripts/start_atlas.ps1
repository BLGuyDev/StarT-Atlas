# Star Technology Atlas launcher (Windows PowerShell 5.1).
# Normally started by double-clicking Start-Atlas.bat in the repo folder.
#   -Check       only report what would be done (python/node, pack folder, missing outputs); changes nothing
#   -Rebuild     force the full data build even if the outputs exist
#   -NoServer    do not start the web server (used by Rebuild-Atlas-Data.bat)
#   -NoBrowser   start the server but do not open the browser
#   -Port N      first port to try (default 8765; the next free one is used if busy)
#   -RunSeconds  stop the server by itself after N seconds (for tests; 0 = run until the window closes)
param(
    [switch]$Check,
    [switch]$Rebuild,
    [switch]$NoServer,
    [switch]$NoBrowser,
    [int]$Port = 8765,
    [int]$RunSeconds = 0
)
$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'
. (Join-Path $PSScriptRoot 'atlas_common.ps1')
$root = $script:RepoRoot
Set-Location -LiteralPath $root
try { $Host.UI.RawUI.WindowTitle = 'Star Technology Atlas' } catch { }

$problems = New-Object System.Collections.ArrayList
$proc = $null
$logOut = $null
$logErr = $null

function Stop-Here([string]$msg, [int]$code = 1) {
    Write-Host ''
    Write-Bad $msg
    exit $code
}

try {
    Write-Host ''
    Write-Host '==============================================' -ForegroundColor Cyan
    Write-Host '  Star Technology Atlas - local launcher' -ForegroundColor Cyan
    Write-Host '==============================================' -ForegroundColor Cyan
    Write-Host ('  Repo folder: ' + $root)
    if ($Check) { Write-Host '  CHECK MODE: nothing will be installed, built or started.' -ForegroundColor Yellow }

    # ---------- [1/6] Python and Node ----------
    Write-Step 1 6 'Checking Python and Node.js...'
    $py = Get-PythonInfo
    $node = Get-NodeInfo
    $needPy = $false
    if (-not $py) {
        $needPy = $true
        [void]$problems.Add('Python 3.10+ not found')
        Write-Bad 'Python was not found.'
    } elseif (-not $py.Ok) {
        $needPy = $true
        [void]$problems.Add('Python is older than 3.10')
        Write-Bad ('Python {0} is too old; version 3.10 or newer is needed.' -f $py.Version)
    } else {
        Write-Ok ('Python {0} ({1})' -f $py.Version, $py.Exe)
    }
    $missing = Get-MissingOutputs
    $willBuild = ($Rebuild.IsPresent -or $missing.Count -gt 0)
    if ($node) {
        Write-Ok ('Node.js {0}' -f $node.Version)
    } elseif ($willBuild) {
        [void]$problems.Add('Node.js not found (needed for the build)')
        Write-Bad 'Node.js was not found (needed to build the data).'
    } else {
        Write-Warn2 'Node.js was not found (only needed when the data has to be rebuilt).'
    }
    if ($problems.Count -gt 0 -and -not $Check) {
        Show-InstallHelp $needPy ($willBuild -and -not $node)
        exit 1
    }
    if ($py -and $py.Ok) { $env:STAR_PYTHON = $py.Exe }

    # ---------- [2/6] Python packages ----------
    Write-Step 2 6 'Checking Python packages (Pillow, numpy)...'
    $havePkgs = $false
    if ($py -and $py.Ok) {
        $old = $ErrorActionPreference; $ErrorActionPreference = 'Continue'
        & $py.Exe -c 'import PIL, numpy' 2>$null
        $havePkgs = ($LASTEXITCODE -eq 0)
        $ErrorActionPreference = $old
    }
    if ($havePkgs) {
        Write-Ok 'Pillow and numpy are installed.'
    } elseif ($Check) {
        Write-Note 'Would install Pillow and numpy (pip install -r requirements-extract.txt).'
    } else {
        Write-Note 'Installing Pillow and numpy (one-time, quiet)...'
        $old = $ErrorActionPreference; $ErrorActionPreference = 'Continue'
        $req = Join-Path $root 'requirements-extract.txt'
        & $py.Exe -m pip install -q --disable-pip-version-check -r $req
        if ($LASTEXITCODE -ne 0) {
            Write-Note 'Retrying for the current user only...'
            & $py.Exe -m pip install -q --disable-pip-version-check --user -r $req
        }
        $code = $LASTEXITCODE
        $ErrorActionPreference = $old
        if ($code -ne 0) {
            Stop-Here ('Could not install Pillow and numpy. Open a terminal and run:  py -m pip install Pillow numpy   (needs internet).')
        }
        Write-Ok 'Installed.'
    }

    # ---------- [3/6] Star Technology folder ----------
    Write-Step 3 6 'Finding your Star Technology folder (the one with mods and kubejs)...'
    $cfg = Read-LocalConfig
    $pack = $null
    $source = ''
    $saveCfg = $false
    if ($env:STAR_PACK_DIR) {
        if (Test-PackDir $env:STAR_PACK_DIR) { $pack = $env:STAR_PACK_DIR; $source = 'STAR_PACK_DIR environment variable' }
        else { Write-Warn2 ('STAR_PACK_DIR is set but has no mods + kubejs: ' + $env:STAR_PACK_DIR) }
    }
    if (-not $pack -and $cfg.Contains('pack_dir')) {
        $cp = [string]$cfg['pack_dir']
        if (Test-PackDir $cp) { $pack = $cp; $source = 'extract\config.local.json' }
        else { Write-Warn2 ('Saved folder no longer valid: ' + $cp) }
    }
    $cands = @()
    if (-not $pack) {
        $cands = @(Find-PackCandidates)
        $star = @($cands | Where-Object { $_.Name -match '(?i)star' })
        if ($star.Count -eq 1) { $pack = $star[0].Path; $source = 'auto-detected' }
        elseif ($star.Count -eq 0 -and $cands.Count -eq 1) { $pack = $cands[0].Path; $source = 'auto-detected' }
        if ($pack) { $saveCfg = $true }
    }
    if (-not $pack) {
        if ($Check) {
            Write-Note ('Would ask you to pick the folder (found {0} candidate folders).' -f $cands.Count)
            foreach ($c in $cands) { Write-Note ('  candidate: ' + $c.Path) }
            [void]$problems.Add('Pack folder not resolved (a folder picker would open)')
        } else {
            if ($cands.Count -gt 1) { Write-Note ('Found {0} possible folders; please choose one.' -f $cands.Count) }
            else { Write-Note 'Could not find it automatically. A window will ask you to pick it.' }
            $start = if ($cands.Count -gt 0) { Split-Path -Parent $cands[0].Path } else { [Environment]::GetFolderPath('MyDocuments') }
            for ($try = 1; $try -le 3 -and -not $pack; $try++) {
                $sel = Select-PackFolder $start
                if (-not $sel) { Stop-Here 'No folder selected. Run the launcher again and choose your Star Technology folder.' }
                if (Test-PackDir $sel) { $pack = $sel; $source = 'you picked it'; $saveCfg = $true }
                else {
                    Write-Bad ('That folder has no "mods" and "kubejs" inside: ' + $sel)
                    Write-Note 'Pick the instance folder itself (for example D:\Games\Star Technology), not its parent or a sub-folder.'
                    $start = $sel
                }
            }
            if (-not $pack) { Stop-Here 'Still not a valid folder. Run the launcher again.' }
        }
    }
    $jar = $null
    if ($pack) {
        Write-Ok ('{0}  [{1}]' -f $pack, $source)
        $jar = Find-VanillaJar $pack $cfg
        if ($jar) { Write-Ok ('Minecraft 1.20.1 jar: ' + $jar) }
        elseif ($Check) { Write-Note 'Minecraft 1.20.1 jar not found (a file picker would open when the build needs it).' }
        elseif ($willBuild) {
            Write-Warn2 'The Minecraft 1.20.1 jar was not found automatically.'
            Write-Note 'A window will ask for it (usually ...\versions\1.20.1\1.20.1.jar in your launcher folder).'
            $jar = Select-VanillaJar
            if (-not $jar) { Stop-Here 'No jar selected. Set STAR_VANILLA_JAR or "vanilla_jar" in extract\config.local.json and run again.' }
            $saveCfg = $true
        }
        if ($saveCfg -and -not $Check) {
            $cfg['pack_dir'] = ConvertTo-Slash $pack
            if ($jar -and -not $env:STAR_VANILLA_JAR) { $cfg['vanilla_jar'] = ConvertTo-Slash $jar }
            Write-LocalConfig $cfg
            Write-Ok 'Saved to extract\config.local.json (you will not be asked again).'
        }
    }

    # ---------- [4/6] Generated data ----------
    Write-Step 4 6 'Checking the generated Atlas data (icons, recipes, 3D blocks)...'
    if ($missing.Count -gt 0) { Write-Note ('Missing: ' + ($missing -join ', ')) }
    else { Write-Ok 'All generated files are present.' }
    if ($Check) {
        if ($willBuild) { Write-Note 'Would run the full build (scripts\build_all.ps1).' } else { Write-Note 'No build needed.' }
    } elseif ($willBuild) {
        if ($Rebuild) { Write-Note 'Full rebuild requested.' }
        Write-Host ''
        Write-Host '      This takes several minutes the first time (it reads every mod jar).' -ForegroundColor Yellow
        Write-Host '      Do not close this window. Lines below are progress messages from the build.' -ForegroundColor Yellow
        $sw = [System.Diagnostics.Stopwatch]::StartNew()
        try {
            & (Join-Path $PSScriptRoot 'build_all.ps1')
        } catch {
            Stop-Here ($_.Exception.Message)
        }
        Set-Location -LiteralPath $root
        $still = Get-MissingOutputs
        if ($still.Count -gt 0) {
            Stop-Here ('The build finished but these files are still missing: ' + ($still -join ', '))
        }
        Write-Ok ('Build finished in {0:mm\:ss}.' -f $sw.Elapsed)
    }

    if ($Check) {
        Write-Host ''
        if ($problems.Count -eq 0) { Write-Host 'CHECK RESULT: ready.' -ForegroundColor Green; exit 0 }
        Write-Host 'CHECK RESULT: problems found:' -ForegroundColor Yellow
        foreach ($p in $problems) { Write-Host ('  - ' + $p) -ForegroundColor Yellow }
        exit 1
    }

    if ($NoServer) {
        Write-Host ''
        Write-Host 'Data is ready. Double-click Start-Atlas.bat to open the Atlas.' -ForegroundColor Green
        exit 0
    }

    # ---------- [5/6] Web server ----------
    Write-Step 5 6 'Starting the local web server...'
    $guia = Join-Path $root 'guia'
    $use = $Port
    while (-not (Test-PortFree $use) -and $use -lt ($Port + 30)) { $use++ }
    if (-not (Test-PortFree $use)) { Stop-Here ('No free port found between {0} and {1}.' -f $Port, ($Port + 30)) }
    if ($use -ne $Port) { Write-Note ('Port {0} is busy; using {1}.' -f $Port, $use) }
    $stamp = [guid]::NewGuid().ToString('N').Substring(0, 8)
    $logOut = Join-Path $env:TEMP ('atlas_http_' + $stamp + '.out.log')
    $logErr = Join-Path $env:TEMP ('atlas_http_' + $stamp + '.err.log')
    $args2 = @('-m', 'http.server', [string]$use, '--bind', '127.0.0.1', '--directory', ('"' + $guia + '"'))
    $proc = Start-Process -FilePath $py.Exe -ArgumentList $args2 -NoNewWindow -PassThru -RedirectStandardOutput $logOut -RedirectStandardError $logErr
    $up = $false
    for ($i = 0; $i -lt 40; $i++) {
        if ($proc.HasExited) { break }
        if (Test-PortOpen $use) { $up = $true; break }
        Start-Sleep -Milliseconds 250
    }
    if (-not $up) {
        $why = ''
        if (Test-Path -LiteralPath $logErr) { $why = (Get-Content -LiteralPath $logErr -ErrorAction SilentlyContinue | Select-Object -First 5) -join ' | ' }
        Stop-Here ('The web server did not start. ' + $why)
    }
    $url = 'http://127.0.0.1:{0}/index.html#plan' -f $use
    Write-Ok ('Serving ' + $guia)

    # ---------- [6/6] Browser ----------
    Write-Step 6 6 'Opening your browser...'
    if ($NoBrowser) { Write-Note ('Skipped (-NoBrowser). Open this address yourself: ' + $url) }
    else {
        try { Start-Process $url; Write-Ok $url }
        catch { Write-Warn2 ('Could not open the browser. Open this address yourself: ' + $url) }
    }

    Write-Host ''
    Write-Host 'Atlas running. 3D: open a module card, press the green 3D assembly line button. Close this window to stop.' -ForegroundColor Green
    Write-Host ('Address: ' + $url)
    $t0 = Get-Date
    while (-not $proc.HasExited) {
        Start-Sleep -Milliseconds 500
        if ($RunSeconds -gt 0 -and ((Get-Date) - $t0).TotalSeconds -ge $RunSeconds) { break }
    }
    if ($proc.HasExited) { Write-Bad 'The web server stopped unexpectedly.'; exit 1 }
}
catch {
    Write-Host ''
    Write-Bad ('Unexpected problem: ' + $_.Exception.Message)
    exit 1
}
finally {
    if ($proc) {
        try { if (-not $proc.HasExited) { & taskkill.exe /PID $proc.Id /T /F 2>$null | Out-Null } } catch { }
    }
    foreach ($f in @($logOut, $logErr)) {
        if ($f -and (Test-Path -LiteralPath $f)) { Remove-Item -LiteralPath $f -Force -ErrorAction SilentlyContinue }
    }
}
