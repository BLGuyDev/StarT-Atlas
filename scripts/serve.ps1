# Serve the Atlas (guia/) at http://127.0.0.1:8765/index.html
Set-Location (Join-Path $PSScriptRoot '..\guia')
Write-Host 'Atlas: http://127.0.0.1:8765/index.html'
python -m http.server 8765 --bind 127.0.0.1
