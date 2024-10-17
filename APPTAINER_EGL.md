# Adaptation for Triton environment
To use Alfred on Triton, we created a container.
This container is built on top of the nvidia/cuda:12.2.2-cudnn8-devel-ubuntu22.04 image and is designed to provide an environment for GPU-accelerated computing with support for headless rendering. The container includes the following key features and tools:
- VirtualGL: VirtualGL is installed to provide the capability for GPU-accelerated remote rendering. This is useful for applications requiring high-performance OpenGL rendering in a virtualized environment.

- EGL Rendering Support: The container is configured for headless rendering using NVIDIA EGL, allowing applications to run without needing an X server. This makes it ideal for remote and GPU-accelerated rendering tasks, including machine learning and 3D applications.

- Xvfb (X Virtual Framebuffer): Xvfb is included to provide a virtual display in environments where a physical display is unavailable. This is useful for running graphical applications in headless mode, allowing them to execute without requiring access to a real display.

- x11vnc: To facilitate remote access to graphical applications, x11vnc is installed. This allows users to access the virtual display provided by Xvfb over VNC, making it easy to manage and visualize applications running in the container remotely.

- Mamba/Conda Package Management: The container includes Miniforge, which provides a lightweight version of Conda for package management. Mamba, a fast alternative to Conda, is also installed, enabling quick installation and management of Python environments and packages.
- Pre-installed Utilities: Common development tools such as git, vim, tmux, htop, curl, and wget are included, along with Python development headers (python3-dev, python3-venv, and python3-pip). 

## Create an apptainer definition file
  Apptainer definition file is equivalent to Dockerfile in the Docker context.

## Submit the job script to build the container image:
```bash
$ sbatch build_apptainer.slurm
```
Different from docker image, in the context of Apptainer, a container image essentially is a `.sif` file.

## Create a virtual conda environment for the project:

In the root directory of the project, where `Vgl-Egl-Xvfb.sif` is, run
```bash
$ apptainer exec --bind $WRKDIR/.conda_pkgs,$WRKDIR/.conda_envs mamba-Xvfb.sif \
  bash -c "mamba env create -p ./myenv -f environment.yml"
```
Mamaba was installed in the container, it is a fast drop-in replacement for Conda, with the same command structure. Remember to bind the .conda_pkgs and .conda_envs folders (assume that you have modified your conda config according to [Triton's docs](https://scicomp.aalto.fi/triton/apps/python-conda/#quick-usage-guide])).
  With the `-p` flag, mamba will create an environment in the specified path, which, in the commnad above, is ./myenv in the present folder.

## Test the container
For detailed commands, necessary environment variable values and expected output, please checkout this 
[notebook](./test_containers.ipynb).


