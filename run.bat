@echo off
echo Starting Local AI Study Assistant...

:: Check if virtual environment exists, if not create it
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    call venv\Scripts\activate
    echo Installing dependencies...
    pip install -r requirements.txt
) else (
    call venv\Scripts\activate
)

:: Launch the Flask App
echo Launching Web Assistant at http://127.0.0.1:5000
start http://127.0.0.1:5000
python app.py
pause