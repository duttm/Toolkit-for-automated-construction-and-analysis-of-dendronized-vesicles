#!/bin/bash

grid=$1

corner=1

skip=1

ions=0 ## number of ions in one dendron

gap=$2
## formula for calculating ions may change in future. 


echo "grid is:" $grid

echo "distance from the corner:" $corner 

echo "skip value is:" $skip

$python_exec package/MembraneMaker_*_*.py package/dppc_3002.gro 1 36468 12 $corner $grid G3_up.gro 1 31 31 G3_down.gro 1 31 31 $skip $gap


rm array.txt array3d.txt array4d.txt den.txt den_down.txt lower_mono.txt store_low_id.txt store_up_id.txt upper_mono.txt write_DEN_new.gro write_DPPC.gro 

$gmx_exec editconf -f combined.gro -o combined.gro -box 30 30 4 -c


##exit
###########################################################################################

input=combined

i=1

GRO="${input}.gro"

tpr=$i-input




# formula for ions for future implementation = number of ions 1 den *  total number of dendrons 

# formula for total number of dendrons = (grid * grid * 2 - 1)

# the above formula will change if : there is any change to distance from the corner, and/or the skip value  


NOD=$(python lookfor.py 2>&1)

echo "DEN     " $NOD

##exit


$gmx_exec editconf -f $GRO -o $tpr -box 30 30 30 -c



GRO=$i-input.gro

tpr=$((++i))-input


top=system.top

$gmx_exec solvate -cp $GRO -cs package/water-box-CG_303K-1bar.gro -box 30 30 30 -radius 0.21 -o $tpr -p system.top


echo "at this point, you need to add the following to the topology file:"

echo "DEN     " $NOD | tee system_dummy.top



let DPPC=3039-NOD

echo "DPPC      " $DPPC | tee -a system_dummy.top

echo "Dont forget the water"

$python_exec insert.py 

echo "i is       " $i

