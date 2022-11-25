#!/usr/bin/env bash
#SBATCH --job-name=G2_ACIDIC
#SBATCH --account=XXXXX
#SBATCH --partition=shared
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4
#SBATCH --time=10:00:00
#SBATCH --output=output.out

export OMPI_TMPDIR="/scratch/$USER/job_$SLURM_JOBID"

##Added local scratch copy 
#cp -r G2_BASE /scratch/$USER/job_$SLURM_JOBID
#cp creator.py /scratch/$USER/job_$SLURM_JOBID
#cp inputs.int /scratch/$USER/job_$SLURM_JOBID

cp -r $SLURM_SUBMIT_DIR/* /scratch/$USER/job_$SLURM_JOBID/


if [ -d Outputs ]; then
  rm -r Outputs
fi
mkdir Outputs


### Change to local scratch for run
cd /scratch/$USER/job_$SLURM_JOBID

module load anaconda3/2020.11
. $ANACONDA3HOME/etc/profile.d/conda.sh
conda activate scw_test
## Please do "conda activate dcw_test" before running this script
module purge
module load slurm
module load cpu
module load gcc/10.2.0
module load openmpi
module load gromacs/2019.6


gmx_exec="mpirun -np 1 gmx_mpi"
python_exec="python"
ntomp="-ntomp 4"
export gmx_exec
export python_exec
export ntomp

$python_exec creator.py inputs.int


cp -r /scratch/$USER/job_$SLURM_JOBID/* $SLURM_SUBMIT_DIR/Outputs

conda deactivate 


