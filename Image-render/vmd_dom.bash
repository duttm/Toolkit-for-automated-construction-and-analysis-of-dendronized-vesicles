#!/bin/bash

tar xvf $6.tar.gz

cp $1 $6

cp $2 $6

margin=$3
vmd=$4
image=$5

cd $6

./run_slurm.bash *.gro *.xtc $margin $vmd $image



exit

