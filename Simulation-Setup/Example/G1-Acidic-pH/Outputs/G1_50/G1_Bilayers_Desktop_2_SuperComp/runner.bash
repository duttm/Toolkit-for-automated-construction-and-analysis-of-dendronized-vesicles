#!/usr/bin/env bash


tar xvf Vesicle_Start.tar.gz

cp 12-input.gro system.top G1_pH_new.itp Vesicle_Start/

cd Vesicle_Start/

sbatch gromacs_prod.job
