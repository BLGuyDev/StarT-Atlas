# Rebuild all generated Atlas data from YOUR Star Technology instance.
# Usage: $env:STAR_PACK_DIR = 'D:/path/to/Star Technology'; ./scripts/build_all.ps1
$ErrorActionPreference = 'Stop'
Set-Location (Join-Path $PSScriptRoot '..')
$env:PYTHONIOENCODING = 'utf-8'

if (-not $env:STAR_PACK_DIR -and -not (Test-Path 'extract/config.local.json')) {
    Write-Error 'Set STAR_PACK_DIR to your Star Technology instance folder (or create extract/config.local.json).'
}

$gt = if ($env:STAR_GT_SRC) { $env:STAR_GT_SRC } else { 'gtsrc' }
if (-not (Test-Path $gt)) {
    Write-Host '== gtsrc/ missing: fetching the StarT GregTech fork sources'
    python extract/fetch_gtsrc.py
    if ($LASTEXITCODE -ne 0) { throw 'fetch_gtsrc.py failed' }
}

function Run([string]$exe, [string[]]$a) {
    Write-Host ''; Write-Host "== $exe $($a -join ' ')"
    & $exe @a
    if ($LASTEXITCODE -ne 0) { throw "$exe $($a -join ' ') failed (exit $LASTEXITCODE)" }
}

Run python @('extract/names.py')            # 1 names.json
Run python @('extract/extract_multis.py')   # 2 multis.json
Run python @('extract/extract_recipes.py')  # 3 recipes.json
Run python @('extract/jar_recipes.py')      # 4 jar_recipes.json
Run python @('extract/gt_machines.py')      # 5 gt_machine_recipes.json
Run python @('extract/build_data.py')       # 6 guia/data/quests.js + multis.js
Run python @('extract/build_recipes_js.py') # 7 guia/data/recipes.js
Run python @('extract/build_assets.py')     # 8 guia/img/atlas.png + data/icons.js + img/m/
Run python @('extract/build_3d.py')         # 9 guia/img/blocks.png + data/blocks3d.js

if (Test-Path 'tools/build_data.js') {
    Run node @('tools/build_data.js')       # 10 wiki data (tools/)
} else {
    Write-Warning 'tools/build_data.js not found - wiki data step NOT run.'
}
Write-Host ''; Write-Host 'Done.'
