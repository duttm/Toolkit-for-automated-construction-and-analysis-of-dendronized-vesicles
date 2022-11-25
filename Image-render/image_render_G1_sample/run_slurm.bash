#!/usr/bin/env bash

gro=$1
xtc=$2
margin=$3
vmd=$4
image=$5

sbatch --export=gro=$gro,xtc=$xtc,margin=$margin,vmd=$vmd,image=$image Slurm_7_26_2022_vmd.bash


