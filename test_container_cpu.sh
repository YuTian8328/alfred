#!/bin/bash

# Start Xvfb in the background
Xvfb :0 -screen 0 1024x768x24 &
# Wait for Xvfb to initialize
sleep 2

# Activate the environment
source activate ./myenv

# Use more threads for rendering
LP_NUM_THREADS=4

# Disable GPU rendering
unset LIBGL_ALWAYS_INDIRECT
unset VGL_DISPLAY
unset VGL_REFRESHRATE

# Run the Python script
python3 verify-gpu-rendering.py
