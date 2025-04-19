@echo off

:: Activate virtual environment if it exists
IF EXIST venv (
    call venv\Scripts\activate
)

:: Install dependencies if needed
pip install -r requirements.txt

:: Run the Flask application
python app.py