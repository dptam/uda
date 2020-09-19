#!/bin/bash

## This is an example of an sbatch script to run a tensorflow script
## using Singularity to run the tensorflow image.
##
## Set the DATA_PATH to the directory you want the job to run in.
##
## On the singularity command line, replace ./test.py with your program
##
## Make a copy of this script and change reserved resources and command to run as needed for your job.
##
## Submit this script using sbatch.

#SBATCH --job-name=tensorflow
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G
#SBATCH --time=4:00:00
#SBATCH --partition=volta-gpu
#SBATCH --output=run-%j.log
#SBATCH --gres=gpu:1
#SBATCH --qos=gpu_access

unset OMP_NUM_THREADS

# Set SIMG path
SIMG_PATH=/nas/longleaf/apps/tensorflow/1.14.0/simg

# Set SIMG name
SIMG_NAME=tensorflow1.14.0-cuda10.0-ubuntu16.04.simg

# Set data path
DATA_PATH=/pine/scr/m/w/mwaldron

# GPU with Singularity
singularity exec --nv -B /pine -B /proj $SIMG_PATH/$SIMG_NAME bash -c "cd $DATA_PATH; ./test.py"

