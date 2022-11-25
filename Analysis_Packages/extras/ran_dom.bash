#!/bin/bash

tar xvf ${3}.tar.gz

cp $1 $3

cp $2 $3

cd $3

./run_slurm.bash *.gro *.xtc

exit

