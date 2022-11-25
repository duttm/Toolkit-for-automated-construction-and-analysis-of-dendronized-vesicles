#!/bin/bash


ionpy=$2
export ionpy

grid=$1

gap=$3

./model.bash $grid $gap
./model_1.bash

rm system_dummy.top
