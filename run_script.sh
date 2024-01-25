#!/bin/bash

# Navigate to the script directory
cd "$(dirname "$0")"

# Pull the latest code from Git
git pull

# Activate the virtual environment
source E:/TickerDataTerritory/tutorial-env/bin/activate

# Install requirements
pip install -r requirements.txt

# Run the Python script
python main.py

# Deactivate the virtual environment
deactivate
