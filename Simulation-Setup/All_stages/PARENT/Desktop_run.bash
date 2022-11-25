#!/usr/bin/env bash


gmx_exec="gmx"
python_exec="python"
ntomp="-ntomp 4"
export gmx_exec
export python_exec
export ntomp

dummy_var1=$2 ## Not used for now
dummy_var2=$3 ## Not used for now


$python_exec creator.py $1


