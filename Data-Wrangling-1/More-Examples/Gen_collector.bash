#!/usr/bin/env bash



python_exec="python3.5"

$python_exec collector.py TA-TA inputs.txt

$python_exec collector.py TA-PO4 inputs.txt

$python_exec collector.py Den_layer_thickness inputs.txt

$python_exec collector.py ROG_DENS_TA inputs.txt

$python_exec collector_DHS_TA.py inputs.txt

$python_exec collector_DHS_all.py inputs.txt
