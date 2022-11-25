#!/bin/bash


i=3

top=system.top

GRO=$i-input.gro

tpr=$((++i))-input

minim=package/npt_1fs.mdp

gmx grompp -f $minim -c $GRO -o $tpr -p $top 

gmx mdrun  -deffnm $tpr -v



GRO=$i-input.gro

tpr=$((++i))-input

minim=package/npt_5fs.mdp

gmx grompp -f $minim -c $GRO -o $tpr -p $top

gmx mdrun -deffnm $tpr -v





