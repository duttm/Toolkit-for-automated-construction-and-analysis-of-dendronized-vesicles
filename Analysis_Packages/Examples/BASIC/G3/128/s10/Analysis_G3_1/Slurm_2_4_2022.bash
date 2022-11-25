#!/usr/bin/env bash
#SBATCH --job-name=G3_Analysis
#SBATCH --account=XXXXX
#SBATCH --partition=shared
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem=12G
#SBATCH --time=15:00:00
#SBATCH --output=output.out



export OMPI_TMPDIR="/scratch/$USER/job_$SLURM_JOBID"

echo "${gro} is here"

echo "${xtc} is here"

Dest=Parent

cp $gro $Dest/
cp $xtc $Dest/

export gro
export xtc

##Added local scratch copy 
cp -r Parent /scratch/$USER/job_$SLURM_JOBID
cp -r Parent_0_1 /scratch/$USER/job_$SLURM_JOBID
cp -r AND /scratch/$USER/job_$SLURM_JOBID
##mv AND/Outputs AND/Outputs_bk
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
skip=1
export gmx_exec
export python_exec
export skip

cd $Dest/

./Wrapper.bash $gro $xtc

cd ../

rm $gro 
rm $xtc

cp -r /scratch/$USER/job_$SLURM_JOBID/AND/Outputs/* $SLURM_SUBMIT_DIR/Outputs/

conda deactivate 


cd $SLURM_SUBMIT_DIR/

rm $gro 
rm $xtc

cd $SLURM_SUBMIT_DIR/$Dest/

rm $gro 
rm $xtc


