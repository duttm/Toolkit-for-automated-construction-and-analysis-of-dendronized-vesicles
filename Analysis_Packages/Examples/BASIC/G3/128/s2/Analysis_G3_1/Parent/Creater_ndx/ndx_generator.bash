#!/bin/bash


##Input and Output files
input_gro=$1
input_xtc=$2
out=DEN.gro
ndx=index
index_folder=Creator_ndx
###################################################
######Pre-processing####################
rm ${ndx}.ndx ${ndx}_mod.ndx
##################################



group=2 ## may change on the basis of gromacs version and some system geometry details. 
######################################################################


echo "$group" | $gmx_exec trjconv -f $input_gro -s $input_gro -o $out

echo "q" | $gmx_exec make_ndx -f $input_gro -o ${ndx}.ndx

cp ${ndx}.ndx ${ndx}_mod.ndx
##################################################################################
NOD=$($python_exec no_of_dens.py  2>&1)
echo "We are going to center as per coordinate: $NOD"
#####################################################################

rm $out 

#######################################################
##skip=3 for now, using as an export variable
group=0
out=centered
printf "center\n$group" | $gmx_exec trjconv -f $input_xtc -s $input_gro -o ${out}.gro -pbc atom -center -ur compact -n ${ndx}_mod.ndx -skip $skip

rm ${ndx}_mod.ndx
rm ${ndx}.ndx
 
## convert -f option to .xtc when the xtc file is available






