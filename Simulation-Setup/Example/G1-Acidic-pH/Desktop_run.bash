#!/usr/bin/env bash





gmx_exec="gmx"
python_exec="python"
ntomp="-ntomp 4"
export gmx_exec
export python_exec
export ntomp

$python_exec creator.py inputs.int


