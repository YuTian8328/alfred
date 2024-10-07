## This script verifies that the GPU rendering is enabled in AI2-THOR 4.0.0
from ai2thor.controller import Controller
from ai2thor.platform import CloudRendering
import time

import logging

# Enable detailed logging
logging.basicConfig(level=logging.DEBUG)

# Initialize the controller with CloudRendering
controller = Controller(
    platform=CloudRendering, 
    width=800, 
    height=600, 
    scene="FloorPlan1",  # You can specify any scene here
    renderDepthImage=True,  # Enable depth rendering
    renderObjectImage=True,  # Enable object mask rendering
    renderClassImage=True,  # Enable class mask rendering
    renderSemanticSegmentation=True  # Enable semantic segmentation
)
print("AI2-THOR controller initialized.")


# Stop the controller when done
controller.stop()
