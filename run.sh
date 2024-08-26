#!/bin/bash

# Check if the virtual environment already exists
if [ -d "venv" ]; then
    echo "Virtual environment found."
else
    # Create a new virtual environment
    echo "Creating a virtual environment..."
    python3 -m venv venv

    # Check if venv creation was successful
    if [ $? -ne 0 ]; then
        echo "Failed to create virtual environment. Ensure Python 3 is installed."
        exit 1
    fi
fi

# Activate the virtual environment
source venv/bin/activate

# Ensure pip is up to date
echo "Upgrading pip to the latest version..."
python3 -m pip install --upgrade pip

# Install the required version of pygame
echo "Installing Pygame 2.6.0..."
pip install pygame==2.6.0

# Check if pygame installation was successful
if [ $? -ne 0 ]; then
    echo "Failed to install Pygame. Please check your internet connection or pip configuration."
    exit 1
fi

# Run the game
echo "Running the game..."
python3 main.py > /dev/null 2>&1 &

# Deactivate the virtual environment
deactivate
