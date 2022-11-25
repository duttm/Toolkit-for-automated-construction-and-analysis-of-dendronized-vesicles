#!/bin/bash

rm centered.gro



#################
storage_in_files=Molecule_Files
in_1=DPPC_details.txt
in_1_1=Molecule_DPPC.txt
in_1_2=Molecule_DPPC_Polar_head.txt
in_2=DEN_details.txt
in_2_1=Molecule_DEN.txt
in_2_2=Molecule_DEN_ALL.txt

cd $storage_in_files/
cp * ../
cd ../
#####################

Dir1=Book_Keeping

if [ -d "$Dir1" ] 
then
    rm -r $Dir1 
fi


Dir2=Outputs

if [ -d "$Dir2" ] 
then
    rm -r $Dir2 
fi

##python_exec=python ## now coming from EXPORT command

$python_exec Codes/driver_1.py $in_1 $in_2 $1

mkdir $Dir1
mv DPPCHEAD* $Dir1 ## at some point needs to be automated 
mv PAMAM* $Dir1 ## at some point needs to be automated 
mkdir $Dir2
mv *.out center_index_number.txt $Dir2

rm $in_1 $in_1_1 $in_1_2 $in_2 $in_2_1 $in_2_2


######

Dir3=IMAGE

if [ -d "$Dir3" ] 
then
    rm -r $Dir3 
fi


mkdir $Dir3

namegro=write
outgro=write_0

$gmx_exec editconf -f ${namegro}.gro -o ${outgro}.gro


./vmd_package/pleaseshowmeavesicle.bash $vmd ${outgro}.gro $image

mv ${outgro}.gro $Dir3
mv *.tga $Dir3


rm *.gro *.tga

rm *#*

## To crop images: On a local hots, type: convert input.tga -trim output.png



###########


