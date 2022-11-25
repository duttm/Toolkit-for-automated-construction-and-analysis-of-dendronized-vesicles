#!/usr/bin/env bash



python_exec="python3"
analysis_direc="Analysis_G2_1"
Combined_output_direc="Comb_Outs"
nameofana="AND_results.out"
generation="G2"


$python_exec final_outputs_collector.py $analysis_direc $Combined_output_direc

$python_exec rename_seeds.py $analysis_direc $Combined_output_direc

$python_exec dump_gen.py $analysis_direc $Combined_output_direc $nameofana $generation
