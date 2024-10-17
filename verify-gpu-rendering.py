from ai2thor.controller import Controller
import torch
import logging
import os
import subprocess
logging.basicConfig(level=logging.DEBUG)
print("starting...")
def verify_opengl_renderer():
    try:
        result = subprocess.run(["vglrun", "glxinfo"], capture_output=True, text=True)
        for line in result.stdout.splitlines():
            if "OpenGL renderer" in line:
                print(f"OpenGL renderer: {line}")  
                return
    except Exception as e:
        print(f"Error when checking OpenGL renderer: {e}")

# Run the verification functions
verify_opengl_renderer()


c = Controller()


# Start the controller with the sanitized environment
c.start()
print("Initialized AI2-THOR with NVIDIA EGL successfully!!!")
event = c.step(dict(action="MoveAhead"))
assert event.frame.shape == (300, 300, 3)
print(event.frame.shape)
print("Everything works!!!")
print("GPU available:", torch.cuda.is_available())
