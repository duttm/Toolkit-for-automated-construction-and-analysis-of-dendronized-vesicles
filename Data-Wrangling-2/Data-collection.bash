#!/usr/bin/env bash



python_exec="python3.5"

cwd=$(pwd)

Collection_Dir=Collection
Pandas_Dir=Pandas

cd $Collection_Dir

$python_exec feature_collection.py $cwd

cd ../$Pandas_Dir


$python_exec dataframe.py $cwd

cp array.txt ../

cd ../$Collection_Dir

rm *.txt

cd ../

## see array.txt

