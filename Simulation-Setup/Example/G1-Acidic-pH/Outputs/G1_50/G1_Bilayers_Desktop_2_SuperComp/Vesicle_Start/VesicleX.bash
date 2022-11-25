#!/bin/bash

module purge
module load slurm
module load cpu
module load gcc/10.2.0
module load openmpi
module load gromacs/2019.6

##exec="mpirun -np 1 gmx_mpi"

###########################################################################################

##i=12

GRO=$i-input.gro

tpr=$((++i))-input

top=system.top

minim=steep.mdp

$exec editconf -f $GRO -o $tpr -box 50 50 50 -c


GRO=$i-input.gro

tpr=$((++i))-input

$exec solvate -cp $GRO -cs package/water-box-CG_303K-1bar.gro -box 50 50 50 -radius 0.21 -o $tpr -p system.top



echo "Now add water to topology"

### point of manual entry 

exit

############################################################################################




