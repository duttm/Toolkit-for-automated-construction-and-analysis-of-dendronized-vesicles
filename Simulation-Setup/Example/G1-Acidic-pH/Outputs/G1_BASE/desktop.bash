#!/bin/bash



gmx_exec="gmx"
python_exec="python"
ntomp="-ntomp 4"
export gmx_exec
export python_exec
export ntomp


grid=$1

./model.bash $grid
./model_1.bash

rm system_dummy.top
