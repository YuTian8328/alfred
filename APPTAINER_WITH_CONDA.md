# Adaptation for Triton environment

## Preparation:
- Modify the test script `scripts/check_thor.py`
- Create an Apptainer`.def` file (equivalent to Dockerfile in the Docker context) to define the environment, which will be used to generate a .sif container file.

## Submit the build_apptainer.slurm job script to build the container image:
```bash
$ sbatch build_conda_apptainer.slurm
```
Different from docker image, in the context of Apptainer, a container essentially is a `.sif` file.

## Create a virtual conda environment for the project:

In the root directory of the project, where `mamba-Xvfb.sif` is, run
```bash
$ apptainer exec --bind $WRKDIR/.conda_pkgs,$WRKDIR/.conda_envs mamba-Xvfb.sif \
  bash -c "mamba env create -p ./myenv -f environment.yml"
```
Mamaba was installed in the container, it is a fast drop-in replacement for Conda, with the same command structure. Remember to bind the .conda_pkgs and .conda_envs folders (assume that you have modified the path according to [Triton's docs](https://scicomp.aalto.fi/triton/apps/python-conda/#quick-usage-guide])).
  With the `-p` flag, mamba will create an environment in the specified path, which, in the commnad above, is ./myenv in the present folder.

## Run (Headless)
After the environment created, request an interactive shell on a gpu node:
```bash
  srun --gpus=1 --mem=40G --pty bash
```

### NOTE: request enough memory, otherwise the python script may hang without any error message!!
#### Start an interactive session in the container
```bash
  apptainer exec --nv mamba-Xvfb.sif bash
```
### inside the container

  #### start a new tmux session
```bash
  tmux new -s startx
```
  #### start X11 server on DISPLAY 0
```bash
  Xvfb :0 -screen 0 1280x1024x24 &
```
  #### detach from tmux shell with Ctrl+b then d

  #### verify the display is on, you are supposed to see two processes, one is for display 0
```bash
  ps aux | grep Xvfb
```
  #### start a new tmux session and a server to stream the display if you want to forward the virtual screen 
  #### to triton desktop to see the real screen, otherwise skip this step and the next step
```bash
  tmux new-session -s vnc_session
  x11vnc -display :0 -forever -rfbport 5999
```
  #### detach from tmux shell with Ctrl+b then d

  #### open a shell in triton desktop https://ondemand.triton.aalto.fi/ to see the real screen
```bash
  vncviewer node_name:5999
```
### back to the previous terminal (still inside the container)
  #### Active the virtual conda environment
```bash
  conda activate ./myenv
```
  #### test thor
```bash  
  python3 scripts/check_thor.py
```
**Expected output**
```bash 
# Initialized AI2-THOR successfully
# (300, 300, 3)
# Everything works!!!
# GPU available: True
```
