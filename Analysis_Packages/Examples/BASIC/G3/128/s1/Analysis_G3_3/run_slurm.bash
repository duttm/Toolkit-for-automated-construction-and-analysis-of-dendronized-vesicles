#!/usr/bin/env bash

gro=$1
xtc=$2

sbatch --export=gro=$gro,xtc=$xtc Slurm_2_4_2022.bash


