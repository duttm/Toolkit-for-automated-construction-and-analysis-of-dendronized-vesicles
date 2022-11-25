#!/bin/bash

## Launch from one folder behind this script
##Usage vmd_package/pleaseshowmeavesicle.bash <name of .vmd script> <name of gro file> <name of image file>


script=$1

gro=$2

image=$3

rm vmd_package/${script}.copy vmd_package/${script}.try2.copy

cp vmd_package/$script vmd_package/${script}.copy

cp vmd_package/${script}.try2 vmd_package/${script}.try2.copy

cp $gro vmd_package/


##TC will remain TC

declare -a arrold=("123456789" "image.tga")

declare -a arrnew=(${gro} ${image}.tga)



for i in {0..1}; do
    echo ${arrold[$i]} ${arrnew[$i]}
    sed -i -e "s/${arrold[$i]}/${arrnew[$i]}/g" vmd_package/${script}.copy vmd_package/${script}.try2.copy
done


vmd -e vmd_package/${script}.copy

###### This section is for interactive VMD #############################

#while true; do
#        read -p "Not happy?" yn
#        case $yn in
#            [Yy]* ) vmd -e vmd_package/$script.try2.copy; break;;
#            [Nn]* ) break;;
#            * ) echo "Please answer yes or no.";;
#        esac
#done

RED='\033[0;31m'

echo -e "${RED}####################################################################################"

echo "Deleting Rudundant Files"
rm vmd_package/$gro

rm vmd_package/${script}.copy vmd_package/${script}.try2.copy

echo "all Done"

echo "please back up your files and images"
