#!/usr/bin/env bash



python_exec="python3"
analysis_direc="Analysis_G1_3"
Combined_output_direc="Comb_Outs"
nameofana="ROG_DENS_TA.out"
generation="G1"


$python_exec final_outputs_collector.py $analysis_direc $Combined_output_direc

$python_exec rename_seeds.py $analysis_direc $Combined_output_direc

$python_exec dump_gen.py $analysis_direc $Combined_output_direc $nameofana $generation
