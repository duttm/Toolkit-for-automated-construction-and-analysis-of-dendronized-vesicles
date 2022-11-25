#!/bin/bash

module purge
module load slurm
module load cpu
module load gcc/10.2.0
module load openmpi
module load gromacs/2019.6



###########################################################################################

let i=i+2

solvate_added=$2

solvate_prev=$1


let total_solvent=solvate_added+solvate_prev

top=system.top


let anti=total_solvent/10



echo "I am gonno add this many number of anti-freeze particles:" $anti



##Lets add anti-freeze particles

GRO=$i-input.gro

tpr=$((++i))-input

minim=package/steep_ions.mdp

$exec grompp -f $minim -c $GRO -o $tpr -p $top

out=$((++i))-input

echo $anti



echo "5" | $exec genion -s $tpr -o $out -p $top -nname WF -nn $anti

##exit

GRO=$i-input.gro

tpr=$((++i))-input

minim=package/steep_ions_anti.mdp

$exec grompp -f $minim -c $GRO -o $tpr -p $top

$exec mdrun -deffnm $tpr -v $ntomp


GRO=$i-input.gro

tpr=$((++i))-input

minim=package/nvt_1fs.mdp

$exec grompp -f $minim -c $GRO -o $tpr -p $top

$exec mdrun -deffnm $tpr -v $ntomp


GRO=$i-input.gro

tpr=$((++i))-input

minim=package/nvt_5fs.mdp

$exec grompp -f $minim -c $GRO -o $tpr -p $top

$exec mdrun -deffnm $tpr -v $ntomp



GRO=$i-input.gro

tpr=$((++i))-input

minim=package/npt_5fs.mdp

$exec grompp -f $minim -c $GRO -o $tpr -p $top

$exec mdrun -deffnm $tpr -v $ntomp


