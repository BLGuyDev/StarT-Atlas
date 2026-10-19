# Rebuild all generated Atlas data from YOUR Star Technology instance.
# Easiest: double-click Start-Atlas.bat (or Rebuild-Atlas-Data.bat) in the repo folder - they call this script.
# By hand (PowerShell, from the repo folder):   .\scripts\build_all.ps1
# The pack folder comes from -PackDir, else $env:STAR_PACK_DIR, else extract\config.local.json.
param(
    [string]$PackDir
)
$ErrorActionPreference = 'Stop'
. (Join-Path $PSScriptRoot 'atlas_common.ps1')
Set-Location -LiteralPath $script:RepoRoot
$env:PYTHONIOENCODING = 'utf-8'
if ($PackDir) { $env:STAR_PACK_DIR = $PackDir }

if (-not $env:STAR_PACK_DIR -and -not (Test-Path 'extract/config.local.json')) {
    throw 'No pack folder set. Run Start-Atlas.bat once (it asks for the folder), or set STAR_PACK_DIR to your Star Technology instance folder (the one that contains mods and kubejs), or create extract/config.local.json.'
}

# Python: the launcher passes STAR_PYTHON; otherwise find one (py -3 or python).
$py = $env:STAR_PYTHON
if (-not $py) {
    $info = Get-PythonInfo
    if (-not $info -or -not $info.Ok) { throw 'Python 3.10 or newer was not found. Install it from https://www.python.org/downloads/ (tick "Add python.exe to PATH") and try again.' }
    $py = $info.Exe
}
$hasBuildJs = Test-Path 'tools/build_data.js'
if ($hasBuildJs -and -not (Get-NodeInfo)) {
    throw 'Node.js was not found (needed for the wiki data and icon ids). Install it from https://nodejs.org/ and try again.'
}

$total = 10
$script:stepNo = 0
$watch = [System.Diagnostics.Stopwatch]::StartNew()

function Run([string]$label, [string[]]$a) {
    $script:stepNo++
    $n = $script:stepNo
    Write-Host ''
    Write-Host ("== Step {0}/{1}: {2}   [{3:mm\:ss} elapsed]" -f $n, $total, $label, $watch.Elapsed) -ForegroundColor Cyan
    & $py @a
    if ($LASTEXITCODE -ne 0) {
        throw ("BUILD FAILED at step {0}/{1} ({2}), exit code {3}. Read the lines just above for the reason, fix it, and run again." -f $n, $total, $label, $LASTEXITCODE)
    }
}

$gt = if ($env:STAR_GT_SRC) { $env:STAR_GT_SRC } else { 'gtsrc' }
if (-not (Test-Path $gt)) {
    Write-Host ''
    Write-Host '== Step 0: gtsrc/ missing - fetching the StarT GregTech fork sources (needs internet)' -ForegroundColor Cyan
    & $py 'extract/fetch_gtsrc.py'
    if ($LASTEXITCODE -ne 0) { throw 'BUILD FAILED at step 0 (extract/fetch_gtsrc.py). Check your internet connection and try again.' }
}

Run 'names (extract/names.py)'                        @('extract/names.py')            # 1 names.json
Run 'multiblocks (extract/extract_multis.py)'         @('extract/extract_multis.py')   # 2 multis.json
Run 'recipes (extract/extract_recipes.py)'            @('extract/extract_recipes.py')  # 3 recipes.json
Run 'jar recipes (extract/jar_recipes.py)'            @('extract/jar_recipes.py')      # 4 jar_recipes.json
Run 'GT machines (extract/gt_machines.py)'            @('extract/gt_machines.py')      # 5 gt_machine_recipes.json
Run 'quests + multis (extract/build_data.py)'         @('extract/build_data.py')       # 6 guia/data/quests.js + multis.js
Run 'recipes.js (extract/build_recipes_js.py)'        @('extract/build_recipes_js.py') # 7 guia/data/recipes.js
Run 'icons (extract/build_assets.py)'                 @('extract/build_assets.py')     # 8 guia/img/atlas.png + data/icons.js + img/m/
Run '3D blocks (extract/build_3d.py)'                 @('extract/build_3d.py')         # 9 guia/img/blocks.png + data/blocks3d.js

if ($hasBuildJs) {
    $node = (Get-NodeInfo).Exe
    $script:stepNo++
    Write-Host ''
    Write-Host ("== Step {0}/{1}: wiki data (tools/build_data.js)   [{2:mm\:ss} elapsed]" -f $script:stepNo, $total, $watch.Elapsed) -ForegroundColor Cyan
    & $node 'tools/build_data.js'                                                       # 10 wiki data (tools/)
    if ($LASTEXITCODE -ne 0) { throw ("BUILD FAILED at step {0}/{1} (tools/build_data.js), exit code {2}." -f $script:stepNo, $total, $LASTEXITCODE) }
} else {
    Write-Warning 'tools/build_data.js not found - wiki data step NOT run.'
}
Write-Host ''
Write-Host ("Done in {0:mm\:ss}." -f $watch.Elapsed) -ForegroundColor Green
