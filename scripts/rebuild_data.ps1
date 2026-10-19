# Rebuild ALL generated Atlas data (icons, recipes, 3D blocks, wiki data) from your Star Technology folder.
# Normally started by double-clicking Rebuild-Atlas-Data.bat in the repo folder.
# Same checks and folder detection as Start-Atlas.bat, but always rebuilds and never starts the server.
#   -Check   only report what would be done
param(
    [switch]$Check
)
$ErrorActionPreference = 'Stop'
$launcher = Join-Path $PSScriptRoot 'start_atlas.ps1'
if ($Check) {
    & powershell.exe -NoProfile -ExecutionPolicy Bypass -File $launcher -Rebuild -NoServer -NoBrowser -Check
} else {
    & powershell.exe -NoProfile -ExecutionPolicy Bypass -File $launcher -Rebuild -NoServer -NoBrowser
}
exit $LASTEXITCODE
