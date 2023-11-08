#!/bin/bash -x
#SBATCH --job-name=g_g_py
#SBATCH --account=jibg31
#SBATCH --nodes=2
#SBATCH --ntasks=1
#SBATCH --time=5:00:00


source /p/scratch/cjibg31/jibg3105/Data/EDWUE/code_edwue/modulesEDWUE.sh


srun -n 1 --mem 2048000 python run_analyses.py

