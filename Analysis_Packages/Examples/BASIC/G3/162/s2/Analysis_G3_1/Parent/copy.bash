#!/bin/bash


#####
Molecule_Repo=Molecule_Files
Molecule_Destination=AND

cp -r $Molecule_Repo ../$Molecule_Destination

cd ../$Molecule_Destination/$Molecule_Repo

mv Molecule.txt Molecule_DPPC.txt



declare -a arrold=("start_DPPC.gro" "Molecule.txt") 

declare -a arrnew=("DPPC_centered.gro" "Molecule_DPPC.txt") 


for i in {0..1} ; do
 
 sed -i -e "s/${arrold[i]}/${arrnew[i]}/g" DPPC_details.txt; ## Simple renaming operations
done

#######################################################################

cp Molecule_DPPC.txt Molecule_DPPC_Polar_head.txt

declare -a arrold=("NC3" "PO4") 

declare -a arrnew=("HEAD" "HEAD") 


for i in {0..1} ; do
 
 sed -i -e "s/${arrold[i]}/${arrnew[i]}/g"  Molecule_DPPC_Polar_head.txt; ## Simple renaming operations
done

###########################################################

cp Molecule_DEN.txt Molecule_DEN_ALL.txt

declare -a arrold=("N0Graft" "P3" "N0" "Qd") 

declare -a arrnew=("ALL" "ALL" "ALL" "ALL") 


for i in {0..3} ; do
 
 sed -i -e "s/${arrold[i]}/${arrnew[i]}/g"  Molecule_DEN_ALL.txt; ## Simple renaming operations
done

#######################################################
