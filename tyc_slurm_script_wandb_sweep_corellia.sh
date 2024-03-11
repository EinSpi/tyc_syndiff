#!/bin/sh
#SBATCH --mail-type=ALL
#SBATCH --mail-user=yichentang777@gmail.com
#SBATCH --job-name=TYC_sweep
#SBATCH --output=TYC_sweep-%A.out 
#SBATCH --error=TYC_sweep-%A.err
#SBATCH --time=0-12:00:00 
#SBATCH --gres=gpu:1  # Number of GPUs if needed#
#SBATCH --mem=24G # Memory in GB 
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --nodelist=corellia

ml miniconda3
source activate syndiff
cd /home/guests/yichen_tang/syndiff
export CC=gcc
export CXX=g++
python wandbsweep.py
ml -miniconda3 # unload all modules
