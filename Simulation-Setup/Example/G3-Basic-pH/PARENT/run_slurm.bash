#!/usr/bin/env bash

inputs=$1
basedir=$2
jobname=$3

sbatch --export=inputs=$inputs,basedir=$basedir,generation=$jobname --output=$jobname.$inputs.slurmout --job-name=$jobname  Slurm_First_Stage.bash


