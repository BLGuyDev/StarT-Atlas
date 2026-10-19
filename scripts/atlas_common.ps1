# Shared helpers for start_atlas.ps1, rebuild_data.ps1 and build_all.ps1 (dot-source this file).
# Windows PowerShell 5.1 compatible, ASCII only, no external modules.

$script:RepoRoot = Split-Path -Parent $PSScriptRoot
$script:ConfigPath = Join-Path $script:RepoRoot 'extract\config.local.json'

# Files the Atlas needs to run with the 3D viewer. All are generated from the user's own pack
# (wiki-data.js comes from tools/build_data.js).
$script:RequiredOutputs = @(
    'guia\data\blocks3d.js',
    'guia\data\icons.js',
    'guia\data\recipes.js',
    'guia\data\wiki-data.js',
    'guia\img\blocks.png',
    'guia\img\atlas.png'
)

# ---------- console output ----------
function Write-Step([int]$n, [int]$total, [string]$text) {
    Write-Host ''
    Write-Host ('[{0}/{1}] {2}' -f $n, $total, $text) -ForegroundColor Cyan
}
function Write-Ok([string]$text)   { Write-Host ('      OK    ' + $text) -ForegroundColor Green }
function Write-Note([string]$text) { Write-Host ('      ' + $text) }
function Write-Warn2([string]$text){ Write-Host ('      WARN  ' + $text) -ForegroundColor Yellow }
function Write-Bad([string]$text)  { Write-Host ('      ERROR ' + $text) -ForegroundColor Red }

# ---------- Python / Node ----------
# Returns @{ Exe; Version; Ok } for the first usable python, preferring one that is >= 3.10.
# Ignores the Windows Store "python.exe" stub (it prints nothing and fails).
function Get-PythonInfo {
    $found = $null
    foreach ($c in @(@('py', '-3'), @('python'))) {
        $cmd = Get-Command $c[0] -ErrorAction SilentlyContinue | Select-Object -First 1
        if (-not $cmd) { continue }
        $a = @()
        if ($c.Count -gt 1) { $a += $c[1..($c.Count - 1)] }
        $a += '-c'
        $a += "import sys;print(sys.executable);print('%d.%d.%d'%sys.version_info[:3])"
        $old = $ErrorActionPreference; $ErrorActionPreference = 'Continue'
        $out = @()
        try { $out = @(& $cmd.Source @a 2>$null) } catch { $out = @() }
        $code = $LASTEXITCODE
        $ErrorActionPreference = $old
        if ($code -ne 0 -or $out.Count -lt 2) { continue }
        $exe = ([string]$out[0]).Trim()
        $ver = $null
        try { $ver = [version](([string]$out[1]).Trim()) } catch { continue }
        if (-not (Test-Path -LiteralPath $exe)) { continue }
        $info = New-Object psobject -Property @{ Exe = $exe; Version = $ver; Ok = ($ver -ge [version]'3.10') }
        if ($info.Ok) { return $info }
        if (-not $found) { $found = $info }
    }
    return $found
}

function Get-NodeInfo {
    $cmd = Get-Command node -ErrorAction SilentlyContinue | Select-Object -First 1
    if (-not $cmd) { return $null }
    $old = $ErrorActionPreference; $ErrorActionPreference = 'Continue'
    $out = @()
    try { $out = @(& $cmd.Source --version 2>$null) } catch { $out = @() }
    $code = $LASTEXITCODE
    $ErrorActionPreference = $old
    if ($code -ne 0 -or $out.Count -lt 1) { return $null }
    return New-Object psobject -Property @{ Exe = $cmd.Source; Version = ([string]$out[0]).Trim() }
}

function Show-InstallHelp([bool]$needPython, [bool]$needNode) {
    Write-Host ''
    Write-Host 'Please install what is missing, then double-click the launcher again:' -ForegroundColor Yellow
    if ($needPython) {
        Write-Host ''
        Write-Host '  Python 3.10 or newer'
        Write-Host '    Download: https://www.python.org/downloads/'
        Write-Host '    IMPORTANT: on the first installer screen tick "Add python.exe to PATH".'
        Write-Host '    Or, in a terminal:  winget install -e --id Python.Python.3.12'
    }
    if ($needNode) {
        Write-Host ''
        Write-Host '  Node.js (LTS)'
        Write-Host '    Download: https://nodejs.org/'
        Write-Host '    Or, in a terminal:  winget install -e --id OpenJS.NodeJS.LTS'
    }
    Write-Host ''
    Write-Host '  After installing, close this window and open the launcher again (a new window sees the new install).'
}

# ---------- pack folder ----------
function Test-PackDir([string]$p) {
    if (-not $p) { return $false }
    try {
        return ((Test-Path -LiteralPath (Join-Path $p 'mods') -PathType Container) -and
                (Test-Path -LiteralPath (Join-Path $p 'kubejs') -PathType Container))
    } catch { return $false }
}

# Returns candidate instance folders (objects with Path and Name) that contain both mods and kubejs.
function Find-PackCandidates {
    $list = New-Object System.Collections.ArrayList
    $seen = @{}
    $add = {
        param([string]$path, [string]$name)
        if (-not (Test-PackDir $path)) { return }
        $full = [System.IO.Path]::GetFullPath($path).TrimEnd('\')
        $key = $full.ToLowerInvariant()
        if ($seen.ContainsKey($key)) { return }
        $seen[$key] = $true
        [void]$list.Add((New-Object psobject -Property @{ Path = $full; Name = $name }))
    }

    # The repo itself may live inside the instance folder: walk up a few levels.
    $d = $script:RepoRoot
    for ($i = 0; $i -lt 3; $i++) {
        $d = Split-Path -Parent $d
        if (-not $d) { break }
        & $add $d (Split-Path -Leaf $d)
    }

    # CurseForge: <root>\curseforge\minecraft\Instances\<name>
    $docs = [Environment]::GetFolderPath('MyDocuments')
    foreach ($base in @((Join-Path $env:USERPROFILE 'curseforge\minecraft\Instances'),
                        (Join-Path $docs 'curseforge\minecraft\Instances'))) {
        if ($base -and (Test-Path -LiteralPath $base)) {
            foreach ($dir in @(Get-ChildItem -LiteralPath $base -Directory -ErrorAction SilentlyContinue)) {
                & $add $dir.FullName $dir.Name
            }
        }
    }

    # Prism Launcher: %APPDATA%\PrismLauncher\instances\<name>\.minecraft (or \minecraft)
    if ($env:APPDATA) {
        $pr = Join-Path $env:APPDATA 'PrismLauncher\instances'
        if (Test-Path -LiteralPath $pr) {
            foreach ($dir in @(Get-ChildItem -LiteralPath $pr -Directory -ErrorAction SilentlyContinue)) {
                & $add (Join-Path $dir.FullName '.minecraft') $dir.Name
                & $add (Join-Path $dir.FullName 'minecraft') $dir.Name
            }
        }
    }
    return $list.ToArray()
}

function Select-PackFolder([string]$startPath) {
    $title = 'Select your Star Technology instance folder (the one that contains mods and kubejs)'
    $picked = $null
    try {
        Add-Type -AssemblyName System.Windows.Forms
        [System.Windows.Forms.Application]::EnableVisualStyles()
        $owner = New-Object System.Windows.Forms.Form
        $owner.TopMost = $true
        $owner.ShowInTaskbar = $false
        $owner.StartPosition = 'CenterScreen'
        $owner.Size = New-Object System.Drawing.Size(1, 1)
        $dlg = New-Object System.Windows.Forms.FolderBrowserDialog
        $dlg.Description = $title
        $dlg.ShowNewFolderButton = $false
        if ($startPath -and (Test-Path -LiteralPath $startPath)) { $dlg.SelectedPath = $startPath }
        $owner.Show()
        $owner.Activate()
        if ($dlg.ShowDialog($owner) -eq [System.Windows.Forms.DialogResult]::OK) { $picked = $dlg.SelectedPath }
        $owner.Close()
        $owner.Dispose()
        $dlg.Dispose()
    } catch {
        Write-Warn2 'Could not open the folder window; type the path instead.'
        $picked = Read-Host '      Full path of your Star Technology folder (empty to cancel)'
        if ($picked) { $picked = $picked.Trim().Trim('"') }
    }
    return $picked
}

# ---------- extract/config.local.json (JSON without BOM) ----------
function Read-LocalConfig {
    $h = New-Object System.Collections.Specialized.OrderedDictionary
    if (Test-Path -LiteralPath $script:ConfigPath) {
        try {
            $raw = [System.IO.File]::ReadAllText($script:ConfigPath)
            $o = $raw | ConvertFrom-Json
            if ($o) { foreach ($p in $o.PSObject.Properties) { $h[$p.Name] = $p.Value } }
        } catch {
            Write-Warn2 'extract\config.local.json is not valid JSON; it will be replaced.'
            $h = New-Object System.Collections.Specialized.OrderedDictionary
        }
    }
    return ,$h
}

function Write-LocalConfig($h) {
    $parts = @()
    foreach ($k in $h.Keys) {
        $v = $h[$k]
        if ($v -is [string]) {
            $s = '"' + (($v -replace '\\', '\\') -replace '"', '\"') + '"'
        } else {
            $s = ConvertTo-Json -InputObject $v -Compress
        }
        $parts += ('  "{0}": {1}' -f $k, $s)
    }
    $json = "{`n" + ($parts -join ",`n") + "`n}`n"
    $dir = Split-Path -Parent $script:ConfigPath
    if (-not (Test-Path -LiteralPath $dir)) { New-Item -ItemType Directory -Path $dir | Out-Null }
    [System.IO.File]::WriteAllText($script:ConfigPath, $json, (New-Object System.Text.UTF8Encoding($false)))
}

function ConvertTo-Slash([string]$p) { return ($p -replace '\\', '/') }

# ---------- vanilla jar ----------
function Find-VanillaJar([string]$pack, $cfg) {
    $c = @()
    if ($env:STAR_VANILLA_JAR) { $c += $env:STAR_VANILLA_JAR }
    if ($cfg -and $cfg.Contains('vanilla_jar')) { $c += [string]$cfg['vanilla_jar'] }
    if ($pack) {
        try { $c += [System.IO.Path]::GetFullPath((Join-Path $pack '..\..\Install\versions\1.20.1\1.20.1.jar')) } catch { }
    }
    $docs = [Environment]::GetFolderPath('MyDocuments')
    $c += (Join-Path $env:USERPROFILE 'curseforge\minecraft\Install\versions\1.20.1\1.20.1.jar')
    $c += (Join-Path $docs 'curseforge\minecraft\Install\versions\1.20.1\1.20.1.jar')
    if ($env:APPDATA) {
        $c += (Join-Path $env:APPDATA 'PrismLauncher\libraries\com\mojang\minecraft\1.20.1\minecraft-1.20.1-client.jar')
        $c += (Join-Path $env:APPDATA '.minecraft\versions\1.20.1\1.20.1.jar')
    }
    foreach ($p in $c) {
        if ($p -and (Test-Path -LiteralPath $p -PathType Leaf)) { return $p }
    }
    return $null
}

function Select-VanillaJar {
    try {
        Add-Type -AssemblyName System.Windows.Forms
        $dlg = New-Object System.Windows.Forms.OpenFileDialog
        $dlg.Title = 'Select the Minecraft 1.20.1 jar (1.20.1.jar)'
        $dlg.Filter = 'Minecraft jar (*.jar)|*.jar'
        $owner = New-Object System.Windows.Forms.Form
        $owner.TopMost = $true
        $owner.ShowInTaskbar = $false
        $owner.Show()
        $r = $dlg.ShowDialog($owner)
        $owner.Close()
        if ($r -eq [System.Windows.Forms.DialogResult]::OK) { return $dlg.FileName }
    } catch { }
    return $null
}

# ---------- generated outputs ----------
function Get-MissingOutputs {
    $m = @()
    foreach ($f in $script:RequiredOutputs) {
        if (-not (Test-Path -LiteralPath (Join-Path $script:RepoRoot $f) -PathType Leaf)) { $m += ($f -replace '\\', '/') }
    }
    return ,$m
}

# ---------- ports ----------
function Test-PortFree([int]$port) {
    $l = $null
    try {
        $l = New-Object System.Net.Sockets.TcpListener([System.Net.IPAddress]::Parse('127.0.0.1'), $port)
        $l.Start()
        return $true
    } catch { return $false } finally { if ($l) { try { $l.Stop() } catch { } } }
}

function Test-PortOpen([int]$port) {
    $c = New-Object System.Net.Sockets.TcpClient
    try {
        $iar = $c.BeginConnect('127.0.0.1', $port, $null, $null)
        if ($iar.AsyncWaitHandle.WaitOne(300) -and $c.Connected) { return $true }
        return $false
    } catch { return $false } finally { $c.Close() }
}
