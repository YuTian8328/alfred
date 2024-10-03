#!/bin/bash
#SBATCH --job-name=build_apptainer
#SBATCH --time=00:30:00
#SBATCH --mem=80G
#SBATCH --cpus-per-task=4

apptainer build ai2thor-Xvfb.sif ai2thor-Xvfb.def
