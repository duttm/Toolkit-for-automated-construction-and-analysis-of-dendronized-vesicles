## Data Structure for Systematic Storage and Analysis

**The issue**: We have run simulations on 3 HPC resources over the course of 1 year. Hence, the data is heterogenously distributed across 3 machines.

**Solution**: We use shell scripts to collect the data from the 3 machines and consolidate it into a well-defined data structure. 

Our scripts organize all files into the following data structure: 

```
DATA/pH/Generation/Concentration/Seeds
```

We have separate data collection/parser scripts for all generations. Separate scripts were required as the file naming was not consistent for all generations. 

## Required Inputs for Parser scripts

Variable  | Sample Input | Comments
| :---: |:---: | :---:
analysis_direc | Analysis_G1_3 | Name of directory that has the analysis files
destination | /path/to/local-directory/DATA/BASIC/G1 | Name of the target directory on the local machine 
inputfilename | G2.err | The slurm .err file. This file has information on the important GROMACS files (.gro and .xtc)

## Running instructions

```
python G1xDATAxparser.py
```

If the script generates some redundant subdirectories in your target directory, you can use: 

```
python deletexempty.py
```

## How does the code work?

Original file naming: Simulation files were stored as Generation-concentration-seed. For example, G1-200-s1. However, the file naming varied in different HPC matchines (G1_200_s1, G1-200_s1, etc.)

To parse these files into a consistent data structure, our scripts do the following: 

```
Parser (files to parse, target directory)

{
## This is a representative function. The user provides information on 
a. what files need to be parsed
b. the final target destination

1. Identify a trend in the naming structure (In G1-200_s1, the hyphen separates the generation and concentration value.
Whereas the underscore separates the concentration and seed value.) 
2. Append the concentartions into an array. 
3. Append the number of seeds associated with each concentration value into separate arrays. 
4. In the target directory, create sub directories in the format Generation/Concenetration/Seed. 
5. Transfer the files to the correct sub directories. 
6. Delete all the redundant directories (if created)
}
```

