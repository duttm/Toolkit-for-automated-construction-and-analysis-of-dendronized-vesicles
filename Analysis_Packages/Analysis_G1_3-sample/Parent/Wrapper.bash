#!/bin/bash


##last exec:./Wrapper.bash name.gro name.xtc
#####
input=$gro
input1=$xtc
######

P=Parent
P1=Parent_0_1
P2=AND
###################

##gmx_exec="gmx"
##python_exec="python"
##export gmx_exec
##export python_exec
###########################
##Temporary measure for lighter/shorter trajectories
##skip=3
##export skip
######
V=Vesicle_Render
V_script=lipid_render.bash
###############
I=Index_Finder
I_python=compile.bash
I1=Molecule_Files/DPPC_details.txt
I2=Molecule_Files/Molecule.txt
#############################
O=Outputs
O_file=center_index_number.txt
#########################
C=Creater_ndx
C_script=ndx_generator.bash
C_out=centered.gro
##############################


cp $input $V/
cp $input $C/
cp $input1 $C/
cp $I1 $I
cp $I2 $I

###############################
cd $V
./$V_script $gro
###############################

cd ../$I
./$I_python
cp "${O}/${O_file}" ../$C
##rm $I1 $I2
##########################

cd ../$C
./$C_script $gro $xtc
cp $C_out ../
rm $1 $2 $C_out $O_file
cd ../

#################################
transfer_gro=centered.gro
dppc_gro=DPPC_centered.gro
den_gro=DEN_centered.gro

cp $C_out ../$P1
cd ../$P1
./Wrapper.bash $transfer_gro 
cp $dppc_gro ../$P2
cp $den_gro ../$P2

rm $transfer_gro
rm $dppc_gro
rm $den_gro


cd ../$P
#######################################

./copy.bash

rm $gro $xtc $transfer_gro
##############
cd ../$P2
./compile.bash

rm -r Book_Keeping/
rm $dppc_gro
rm $den_gro




