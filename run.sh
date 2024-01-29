#!/bin/bash

#SBATCH --exclusive
#SBATCH --nodes=1
#SBATCH --constraint=[v100|p100]
#SBATCH --tasks-per-node=1
#SBATCH --time 8:00:00
#SBATCH --error=job-%A.err
#SBATCH --output=job-%A.out

python run.py "MinAtar/$1-v0"