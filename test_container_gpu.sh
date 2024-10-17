#!/bin/bash

# Start Xvfb in the background
Xvfb :0 -screen 0 1024x768x24 &
# Wait for Xvfb to initialize
sleep 2

# Activate the environment
source activate ./myenv

# Disable GPU rendering
# unset LIBGL_ALWAYS_INDIRECT

# Run the Python script
vglrun python3 verify-gpu-rendering.py
