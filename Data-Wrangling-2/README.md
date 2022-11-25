# DATA-Wrangling-2

In the previous step (`Data-wrangling-1`), we had written the results of all calculations into separate text files. Now, we will systematically merge all the files into a one csv file. This file can be used for exploratory data analysis and machine learning (will be pursued in future). 

## Pre-requisites: 

Keep all `Summary_GX.txt` files in the `DATA` folder. <br> 
Go to `Collection/feature_collection.py` and fill out these input variables:


Variable  | Sample Input | Comments
| :---: |:---: | :---:
PH |  ["ACIDIC", "BASIC"] | Input the pH conditions as a list
FEATURE | ["ROG_DENS_TA", "TA-TA", "TA-PO4"] | Input the names of the calculations as a list
GEN| ["G1", "G2", "G3"] | Input the generation as a list


## Running instructions:

```
./Data-collection.bash
```

This script will produce array.csv (all project results stored in this file). 

## Read the Data

Use the read_array.ipnyb notebook to study the data. 


