## High-throughput Image Generator

We developed this tool to generate filtered images of vesicles. At the end of an MD simulation, we get systems where the majority of the molecules assemble to form a vesicle. However, a few molecules form smaller aggregates around the vesicle. Additionally, the vesicle is not at the center of the periodic box at the end of the simulation. To automate image generation for 400+ vesicles, we developed this tool that can do the following: 

1. Eliminate coordinates of molecules that are not a part of the vesicle (remove noise)
2. Center the vesicle 
3. Render the focused and cleaned up image using VMD 
4. Reproduce the process for 400+ vesicles using a high-throughput framework

## Prerequisites for running the code:

Python (any version >3) <br>
[VMD](http://www.ks.uiuc.edu/Research/vmd/) <br>
An anaconda session running on a HPC machine <br>

## Running instructions:

The `expanse_image_launcher.py` is the main driver code that will create the framework to generate images for all vesicles in parallel. Within the previously built database (see [Create-Data-Structure](../Create-Data-Structure)), the python script needs to be placed in place of *** 

DATA/pH/Generation/****/Concentration/Seeds

Input variables for `expanse_image_launcher.py` : 

Variable  | Sample Input | Comments
| :---: |:---: | :---:
Generation | G5 | Enter the dendron generation (G1 through G6)
pH | Basic | Enter the pH of the system (Acidic/Basic)
margin | 1.6 | Cut-off distance to remove noise (details below)
vmd  | G1_vescile.vmd | vmd script 


The variable `margin` is introduced to eliminate the molecules that are not a part of the vesicle. A higher value is used for larger generations. 

To run the code, activate an anaconda session on your HPC machine and type 
```
python expanse_image_launcher.py`
```
