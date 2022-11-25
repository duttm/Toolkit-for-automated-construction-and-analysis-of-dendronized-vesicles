#!/usr/bin/env bash

module purge
module load slurm
module load cpu
module load gcc/10.2.0
module load openmpi
module load gromacs/2019.6

SLURM_NPROCS=128

start=20
skip=2
###################### NPT 323K 60 ns 5 fs #####################################

i=$((start+skip-2))

echo $i
GRO=$i-input.gro
tpr=$((++i))-input
minim=npt_5fs_long.mdp
top=system.top
out=$((++i))-input

#Replace below "em" by your input file name

mpirun -np 1 gmx_mpi grompp -f package/$minim  -c $GRO -p $top -o $tpr

mpirun -np $SLURM_NPROCS gmx_mpi mdrun -v -deffnm $out -s $tpr 


###################### NPT 323K 400 ns 10 fs #####################################


i=$((start+skip+0))

echo $i

GRO=$i-input.gro
tpr=$((++i))-input
minim=npt_10fs_extended.mdp
top=system.top
out=$((++i))-input

#Replace below "em" by your input file name

mpirun -np 1 gmx_mpi grompp -f package/$minim  -c $GRO -p $top -o $tpr

mpirun -np $SLURM_NPROCS gmx_mpi mdrun -v -deffnm $out -s $tpr 


######################################################################################
exit

###################### NPT 323K 800 ns 20 fs #####################################
i=$((start+skip+2))

echo $i

GRO=$i-input.gro
tpr=$((++i))-input
minim=npt_20fs_extended.mdp
top=system.top
out=$((++i))-input

#Replace below "em" by your input file name

mpirun -np 1 gmx_mpi grompp -f package/$minim  -c $GRO -p $top -o $tpr

mpirun -np $SLURM_NPROCS gmx_mpi mdrun -v -deffnm $out -s $tpr 


######################################################################################

###################### NPT 323K 800 ns 20 fs #####################################
i=$((start+skip+4))

echo $i

GRO=$i-input.gro
tpr=$((++i))-input
minim=npt_20fs_extended.mdp
top=system.top
out=$((++i))-input

#Replace below "em" by your input file name

##mpirun -np 1 gmx_mpi grompp -f package/$minim  -c $GRO -p $top -o $tpr

##mpirun -np $SLURM_NPROCS gmx_mpi mdrun -v -deffnm $out -s $tpr 


######################################################################################


