#!/bin/bash

##last exec: /lipid_render.bash *.gro

##Input and Output files
input_gro=$1
out=start_DPPC.gro
index_folder=Index_Finder
###################################################

##GROMACS executable
##gmx_exec=gmx ## Now coming from EXPORT command
lipid_group=3 ## may change on the basis of gromacs version and some system geometry details. 
######################################################################


echo "$lipid_group" | $gmx_exec trjconv -f $input_gro -s $input_gro -o $out
mv $out ../$index_folder/

rm *.gro
