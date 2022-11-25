#!/usr/bin/env bash

#SBATCH --account=XXXXX
#SBATCH --partition=shared
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4
#SBATCH --time=10:00:00


export OMPI_TMPDIR="/scratch/$USER/job_$SLURM_JOBID"

echo "${inputs} is here"


######## Copy files to Scratch directory #############################
declare -a filelist=("Slurm_First_Stage.bash" "run_slurm.bash" "creator.py" "Desktop_run.bash")
 
for i in {0..3} ; do
 
 echo ${filelist[i]} | cp -r $SLURM_SUBMIT_DIR/${filelist[i]} /scratch/$USER/job_$SLURM_JOBID/ 
done

cp -r $SLURM_SUBMIT_DIR/$basedir /scratch/$USER/job_$SLURM_JOBID/
cp -r $SLURM_SUBMIT_DIR/$inputs /scratch/$USER/job_$SLURM_JOBID/
#########################################################################
#if [ -d Outputs ]; then
#  rm -r Outputs
#fi

#### Make an output directoy. All required outputs are stored here at the end of the run ###########
mkdir Outputs_${generation}_${inputs}
#########################################################################

### Change to local scratch for run
cd /scratch/$USER/job_$SLURM_JOBID


######### Open Anaconda Session ################################
module load anaconda3/2020.11
. $ANACONDA3HOME/etc/profile.d/conda.sh
conda activate scw_test


###### Load gromacs variables ##############################
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

###### Exceute the main python script that generates the structure ####################

$python_exec creator.py ${inputs}

##################### Copy all the required files to the output directoy ###############

cp -r /scratch/$USER/job_$SLURM_JOBID/* $SLURM_SUBMIT_DIR/Outputs_${generation}_${inputs}


#######################################################################
conda deactivate 


