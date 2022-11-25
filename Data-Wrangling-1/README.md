## Data Wrangling 1 

Here, the objective is to collect all numeric results (mean +- std) from the database (see `Create-Data-Structure`), and transfer it to a well-organized csv file.
We have divided this into 2 steps/folder:
1. `Data-Wrangling-1`: We store results for each calculation pertaining to a specific dendron generation in a separate file. This process generates nearly 100 data files. These files are used for plotting the data as a function of dendron generation and concentration using gnuplot. 
 
2. `Data-Wrangling-2`: Here, all the files are systematically merged into one large csv file. Each data point has nearly 10 features. This file can be used for future machine learning applications.
 
## 2 Step Workflow
 
### Step 1:
To generate well-organized data files, we need to first count the number of data points. The final data file (`Summary_GX.txt`) that will store the numeric results of a calculation (say dendron height) for a specific dendron generation will have the following format: 
 
GENERATION | Concentration | Dendron Height (Mean) |Standard deviation
| :---: |:---: | :---: | :---: 
G1 | 100 | 5 | 0.1
XXX | XXX | XXX | XXX
XXX | YYY | YYY | YYY

 
First, we will count the total number of data points. Later, this information will be channeled to the first 2 columns of the above table. Let’s say, we need to collect data to calculate the average Dendron Height for Generation 1. In that case, the code will parse through the database to look for the observations of dendron height pertaining to generation 1. <br>

Each generation has multiple concentrations, and each concentration has multiple seeds. Our code stores this information in `GX.txt`. The file looks like this: 

Concentration | Number of seeds
| :---: |:---: 
10 | 4
15 | 3
20 | 4
 
 
To generate this file, please use the files in `Count-Datapoints`. As per the layout of the database, these files need to be placed in ****: 
 
```
DATA/pH/Generation/****/Concentration/Seeds
```
 
The wrapper script `Analysis_Gx.bash` will execute 3 python scripts in sequential order. The final out will be GX.txt which will enlist all the concentrations, and the number of seeds for each concentration.
 
Input requirements for  `Analysis_GX.bash`: 
 
 
Variable  | Sample Input | Comments
| :---: |:---: | :---:
python_exec | python3 | Use anything >3
analysis_direc | Analysis_G2_1 | Name of the analysis directory where the observations are stored
Combined_output_direc | Comb_Outs | The code will create a new directory to store the raw observations. This comes in handy when there are multiple analysis directories such as Analysis_G2_1 and Analysis_G2_3.
nameofana |  AND_results.out  | Name of the file where the raw observations are stored
generation |  G2 | Dendron generation

Running instructions: 
 
```
./Analysis_Gx.bash   ## run this bash script
``` 
 
How does the code work? 
 
The script `Analysis_Gx.bash` launches 3 steps to get `GX.txt` that has details of the concentrations and associated seeds. 
 
```
These scripts are launched sequentially:
1. final_outputs_collector.py: Count the concentration values and the associated number of seeds. 
2. rename_seeds.py: Re-number the seeds sequentially (for example: convert "S1, S4, S5" to "S1, S2, S3")
3. dump_gen.py: Write concentration and seed information systematically in GX.txt 
```

### Step 2: 
Once we know the concentration and associated number of seeds, we can collect the mean and standard deviation values for each calculation. Typically, a single seed has 100 observations (100 measurements of dendron height). If there are 4 seeds, we have a total of 400 observations for each concentration. Our code takes the average of all observations and reports a mean and standard deviation. These values are dumped into a data file called `Summary_GX.txt` (described above).

To generate this file, please use the files in `Collect-Data`. As per the layout of the database, these files need to be placed in ****: 
 
DATA/pH/****/Generation/Concentration/Seeds
 
The wrapper script `Gen_ves_dim.bash` will generate 10 folders, each containing Summary_GX.txt files for a specific calculation (vesicle-radius, dendron-height, etc).

Running instructions: 
 
```
./Gen_ves_dim.bash
 
```
 
How does the code work?: 
 
```
Generate summary data (calculation)
 
## This is a representation function showcasing how a summary data file is created
## The input for this function will be the name of a calculation such as “vesicle-dimension”
 
1. Read GX.txt and find a concentration value. 
2. Count the associated number of seeds for the concentration value.
3. Append the raw observables from all seeds into an array
4. Compute the mean and standard deviation
5. Write the computed values to Summary_GX.txt
6. Repeat steps 1 to 5 for all concentration values.  
 
```

## Extra notes

The `Collect-Data` folder has information on collecting data for 10 types of calculations. More calculations are provided in `More-Examples`

