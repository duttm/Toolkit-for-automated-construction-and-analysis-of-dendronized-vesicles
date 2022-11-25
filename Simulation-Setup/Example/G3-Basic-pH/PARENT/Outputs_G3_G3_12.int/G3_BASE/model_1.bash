#!/bin/bash


i=2

top=system.top

GRO=$i-input.gro

tpr=$((++i))-input

minim=package/steep_ions.mdp

$gmx_exec grompp -f $minim -c $GRO -o $tpr -p $top 

$gmx_exec mdrun  -deffnm $tpr -v $ntomp



GRO=$i-input.gro

tpr=$((++i))-input

minim=package/nvt_1fs.mdp

$gmx_exec grompp -f $minim -c $GRO -o $tpr -p $top

$gmx_exec mdrun -deffnm $tpr -v $ntomp


GRO=$i-input.gro

tpr=$((++i))-input

minim=package/nvt_5fs.mdp

$gmx_exec grompp -f $minim -c $GRO -o $tpr -p $top

$gmx_exec mdrun -deffnm $tpr -v $ntomp



GRO=$i-input.gro

tpr=$((++i))-input

minim=package/npt_5fs.mdp

$gmx_exec grompp -f $minim -c $GRO -o $tpr -p $top

$gmx_exec mdrun -deffnm $tpr -v $ntomp

