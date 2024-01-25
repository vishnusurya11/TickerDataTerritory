@echo off
REM Change directory to the batch file's location
cd %~dp0
REM Pull the latest code from Git
git pull
call tutorial-env\Scripts\activate
REM Install requirements
pip install -r requirements.txt
REM Run the Python script using the Python interpreter from the virtual environment
E:\TickerDataTerritory\tutorial-env\Scripts\python main.py
deactivate
