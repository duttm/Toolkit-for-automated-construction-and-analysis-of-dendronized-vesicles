#!/bin/bash


##last exec:./Wrapper.bash *.gro 
#####
input=$1
######



######
V=Vesicle_Render
V_script=lipid_render.bash
V1_script=dendron_render.bash
###############
cp $input $V/
###############################
cd $V
./$V_script *.gro
./$V1_script *.gro
###############################



