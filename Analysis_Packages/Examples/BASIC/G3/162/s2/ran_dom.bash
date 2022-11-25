#!/bin/bash

tar xvf Analysis_G3_3.tar.gz

cp $1 Analysis_G3_3/

cp $2 Analysis_G3_3/

cd Analysis_G3_3/

./run_slurm.bash *.gro *.xtc

exit

