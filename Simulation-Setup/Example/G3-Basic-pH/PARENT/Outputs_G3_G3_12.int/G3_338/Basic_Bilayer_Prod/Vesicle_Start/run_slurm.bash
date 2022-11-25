#!/usr/bin/env bash

TOP=$1
ITP=$2
jobname=$3

sbatch --export=TOP=$TOP,ITP=$ITP --output=$jobname.slurmout --job-name=$jobname  gromacs_prod.job


