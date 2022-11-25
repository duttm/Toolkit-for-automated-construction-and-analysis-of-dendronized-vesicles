#!/usr/bin/env bash




declare -a arrold=("G1" "G2" "G3" "G4" "G5" "G6") ## C36 parameters



 
for i in {0..5} ; do
 
 echo ${arrold[i]} | paste "../AND_results/Summary${arrold[i]}.txt" "../ROG_DENS_TA/Summary${arrold[i]}.txt" | column -s $' ' -t >"${arrold[i]}_test.txt"
 echo ${arrold[i]} | awk '{print $1,$2,$3,$4,$7,$8}' "${arrold[i]}_test.txt" > "Summary${arrold[i]}.txt"
done

rm *test*


