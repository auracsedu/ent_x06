# Usage: .\setup.ps1            (default: latest Python 3 via py launcher)
#        .\setup.ps1 -Python 3.12
param([string]$Python = "3")

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

if (-not (Test-Path .venv)) { py "-$Python" -m venv .venv }

$venvPython = ".\.venv\Scripts\python.exe"
& $venvPython -m pip install --upgrade pip
& $venvPython -m pip install -r requirements.txt
& .\.venv\Scripts\Activate.ps1

Write-Host "Done"
