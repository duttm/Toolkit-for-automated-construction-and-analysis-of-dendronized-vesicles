#!/usr/bin/env bash
#SBATCH --job-name=G1_VMD
#SBATCH --account=XXXXX
#SBATCH --partition=shared
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem=1G
#SBATCH --time=00:05:00
#SBATCH --output=output.out

export OMPI_TMPDIR="/scratch/$USER/job_$SLURM_JOBID"


echo "${gro} is here"

echo "${xtc} is here"

Dest=Parent

cp $gro $Dest/
cp $xtc $Dest/



export gro
export xtc
export margin

cp -r Parent /scratch/$USER/job_$SLURM_JOBID
cp -r Parent_0_1 /scratch/$USER/job_$SLURM_JOBID
cp -r AND /scratch/$USER/job_$SLURM_JOBID

mkdir Outputs
mkdir IMAGE


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
module load vmd 



gmx_exec="mpirun -np 1 gmx_mpi"
python_exec="python"
skip=1000
export gmx_exec
export python_exec
export skip
export vmd
export image

## To crop images: On a local hots, type: convert input.tga -trim output.png
cd $Dest
./Wrapper.bash $gro $xtc $margin

cd ../

rm $gro 
rm $xtc

cp -r /scratch/$USER/job_$SLURM_JOBID/AND/Outputs/* $SLURM_SUBMIT_DIR/Outputs/
cp -r /scratch/$USER/job_$SLURM_JOBID/AND/IMAGE/* $SLURM_SUBMIT_DIR/IMAGE/

conda deactivate 


cd $SLURM_SUBMIT_DIR/

rm $gro 
rm $xtc

cd $SLURM_SUBMIT_DIR/$Dest/

rm $gro 
rm $xtc




