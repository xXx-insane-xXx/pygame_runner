#!/bin/bash

# Check if the virtual environment exists
if [ ! -d "venv" ]; then
    echo "Error: Virtual environment not found. Please ensure the venv directory is included."
    exit 1
fi

# Activate the virtual environment
source venv/bin/activate

# Run the game
venv/bin/python3 main.py > /dev/null 2>&1 &

# Deactivate the virtual environment (optional)
deactivate
