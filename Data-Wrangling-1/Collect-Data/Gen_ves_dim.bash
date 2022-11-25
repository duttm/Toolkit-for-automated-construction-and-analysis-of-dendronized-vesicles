#!/usr/bin/env bash



python_exec="python3.5"



$python_exec collector_outside_rad.py inputs.txt

mv DPPC_vesicle_status Outer_Vesicle_Rad

$python_exec collector_inside_rad.py inputs.txt

mv DPPC_vesicle_status Inner_Vesicle_Rad

$python_exec collector_thickness_bilayer.py inputs.txt

mv DPPC_vesicle_status Thickness_Bilayer


$python_exec collector_asymmetry.py inputs.txt

mv DEN_vesicle_status asymmetry


$python_exec collector_outside.py inputs.txt

mv DEN_vesicle_status outside


$python_exec collector_inside.py inputs.txt

mv DEN_vesicle_status inside


$python_exec collector_expelled.py inputs.txt

mv DEN_vesicle_status expelled

$python_exec collector.py AND_results inputs.txt

$python_exec collector.py packing_factor inputs.txt

$python_exec collector.py hydrophobic_vol inputs.txt
