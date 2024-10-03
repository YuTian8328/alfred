# Adaptation for Triton environment

## Preparation:
- Modify the test script `scripts/check_thor.py`
- Create an Apptainer`.def` file (equivalent to Dockerfile in the Docker context) to define the environment, which will be used to generate a .sif container file.

## Submit the build_apptainer.slurm job script to build the container image:
```bash
$ sbatch build_apptainer.slurm
```
Different from docker image, in the context of Apptainer, a container essentially is a `.sif` file.

## Run (Headless)
Request an interactive shell on a gpu node:
```bash
$ srun --gpus=1 --mem=40G --pty bash
```
NOTE: request enough memory, otherwise the python script may hang without any error message.

Start an interactive session in the container:
```bash
$ apptainer exec --nv ai2thor-Xvfb.sif bash

# inside the container
 # create a virtual environment and install packages needed for the project
 # by default, apptainer will bind the present working folder (along with some system folders) to the container,
 # so this environment is writable and accessible both inside and outside the container
  python3 -m venv --system-site-packages ./myenv
  source ./myenv/bin/activate 
  pip install -r requirements.txt

  # start a new tmux session
  tmux new -s startx

  # start X11 server on DISPLAY 0
  Xvfb :0 -screen 0 1280x1024x24 &

  # detach from tmux shell
  # Ctrl+b then d

  # verify the display is on, you are supposed to see two processes, one is for display 0
  ps aux | grep Xvfb

  # start a new tmux session and a server to stream the display if you want to forward the virtual screen 
  # to triton desktop to see the real screen, otherwise skip this step and the next step

  tmux new-session -d -s vnc_session

  x11vnc -display :0 -forever -rfbport 5999

  # detach from tmux shell
  # Ctrl+b then d

  # open a shell in triton desktop https://ondemand.triton.aalto.fi/ to see the real screen
  vncviewer node_name:5999

  # back to the previous terminal (still inside the container)
  # test thor
  python3 scripts/check_thor.py

############
# Initialized AI2-THOR successfully
# (300, 300, 3)
# Everything works!!!
# GPU available: True
```
