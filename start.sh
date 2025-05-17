# Pfad zum virtuellen Environment anpassen, falls nötig
$venv_path = ".\.venv\Scripts\Activate.ps1"

if (Test-Path $venv_path) {
    Write-Host "Aktiviere virtuelles Environment..."
    & $venv_path
} else {
    Write-Warning "Virtuelles Environment nicht gefunden: $venv_path"
}

Write-Host "Starte Streamlit App..."
streamlit run dashboard/app.py
