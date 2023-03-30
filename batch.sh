#!/bin/bash
#SBATCH --mail-type=ALL 
#SBATCH -t 3:00 # 3 minutes
#SBATCH --mem=1g #1 GB of memeory

module load miniconda
conda activate /gpfs/gibbs/project/phys678/phys678_dcm42/conda_envs/phys678
python calc_pi.py
