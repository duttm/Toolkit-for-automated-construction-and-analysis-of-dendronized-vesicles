# Analysis of Dendronized Vesicles

We have built a python object oriented package to characterize various properties of dendronized vesicles. The input for this package is molecular dynamics simulation trajectories of stable dendronized vesicles. Since we deal with a large phase space of dendronized vesicles (400+ vesicles), the package is designed to simultaneously analyze all vesicles on HPC resources.

## Types of Analysis

Serial No. | Name of Analysis | Description
| :---: | :---: | :---:
1 | Vesicle statistics | Provides the basic dimensions of the vesicle, namely mean radius, outer and inner radius. It also provides a count of the number of lipids in the outer and inner monolayers. Finally, it counts the lipids that are not a part of the vesicle. 
2 | Dendron statistics | Provides a count of the number of dendrons on the outer and inner monolayers. Also, it counts the dendrons that are not a part of the vesicle. 
3 | Average Neighbor Distance (AND) | Computes the average distance between 2 neighboring dendrons in the vesicle.
4 | Packing factor | Computes the packing factor of the lipids on the outer monolayer of the vesicle. (The packing factor measures the average geometry of individual lipids in assemblies.)
5 | Dendron conformation | Calculates the average radius of gyration (effective size) of dendrons
6 | Height of dendrons | Calculates the average height of dendrons. 
7 | Surface area covered by dendrons | Computes the surface area covered by the dendron branches on the outer surface of the vesicle
8 | Interaction count (dendron-dendron) | Counts the number of interactions between dendron branches
9 | Interaction count (dendron-lipid) | Counts the number of interactions between dendron branches and lipids
10 | Extension of dendron branches | Computes the extension of the dendron branches (away from the surface of the vesicle).

  
### Notes:

1. Nearly all dendron-related calculations are performed on the dendrons that are located on the outer surface of the vesicle.  
2. **Adaptivity of code**: All calculations are performed using a reference coordinate on each molecule (dendron or lipid). We have decoupled the choice of reference coordinate from the main code: a separate input text file with information on reference coordinates is used. This means that the user can change the reference coordinates as per the requirement. This feature provides flexibility to perform various other types of calculations.
