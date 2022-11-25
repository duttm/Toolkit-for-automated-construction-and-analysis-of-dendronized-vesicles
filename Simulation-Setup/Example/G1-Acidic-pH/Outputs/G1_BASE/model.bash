#!/bin/bash

grid=$1

corner=1

skip=1

gap=$2



## formula for calculating ions may change in future. 


echo "grid is:" $grid

echo "distance from the corner:" $corner 

echo "skip value is:" $skip


python3 package/Jumlesh_G1_acidic.py package/dppc_3002.gro 1 36468 12 $corner $grid G1_up.gro 1 7 7 G1_down.gro 1 7 7 $skip $gap



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
#######################################################################
let ions=NOD*ionpy

echo "I am putting these many number of ions": $ions
#######################################################################

$gmx_exec editconf -f $GRO -o $GRO -box 30 30 30 -c
$gmx_exec insert-molecules -ci package/single_Cl.gro -f $GRO -nmol $ions -try 10 -o $tpr

GRO=$i-input.gro

tpr=$((++i))-input


top=system.top

$gmx_exec solvate -cp $GRO -cs package/water-box-CG_303K-1bar.gro -box 30 30 30 -radius 0.21 -o $tpr -p system.top


echo "at this point, you need to add the following to the topology file:"

echo "DEN     " $NOD | tee system_dummy.top



let DPPC=3039-NOD

echo "DPPC      " $DPPC | tee -a system_dummy.top

echo "Cl       " $ions | tee -a system_dummy.top

echo "Dont forget the water"

python insert.py 

echo "i is       " $i

