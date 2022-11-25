#!/bin/bash

in=DPPC_details.txt
out=start_DPPC.gro
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

$python_exec Codes/driver.py $in

mkdir $Dir1
mv DPPCHEAD* $Dir1 ## at some needs to be automated 

mkdir $Dir2
mv status_writer.txt vesicle_status.txt center_index_number.txt $Dir2
rm $out
rm *.txt

