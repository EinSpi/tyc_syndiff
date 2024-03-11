
import os
print(os.getenv('SLURM_NODELIST').split()[0])
print(os.getenv('SLURM_NODELIST').split())
print(os.getenv('SLURM_NODELIST'))

print(os.getenv('SLURM_NTASKS'))
print(os.getenv('SLURM_PROCID'))
print(int(os.getenv('SLURM_NTASKS'))//int(os.getenv('SLURM_JOB_NUM_NODES')))




