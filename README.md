# ACO_path_planning
## Basics

This repo provides a Python implementation of the Ant Colony Optimization Algorithm for path planning purposes. The ant colony optimization algorithm implemented in this repo is the Ant System Algorithm.

## Description

The package is made up by two directories:

- The aco directory: contains the ant_colony class for handling the ant colony optimization algorithm and the map_class class for handling the operations with the map.

- The maps directory: contains the maps to calculate the path from.

### Usage

The user will pass to the program the number of iterations, ants,map, p,Q and if the map and result is displayed graphically or not.

- p: is the pheromone's evaporation rate, [0-1]
- Q: is the pheromone adding constant.

Information regarding how the program is executed is displayed when executing from the command line:
python aco_resolve_path.py --help

### Map construction

The maps have to be included in the maps directory. For a map to be valid, it must meet the following requirements:

- mxm map, square matrix shape.
- S indicates the starting point, just one starting point is allowed.
- F indicates the final point, just one final point is allowed.
- E indicates if a point in the map is empty.
- O indicates if a point in the map is occupied.

## Result example

A resulting path would be the following:

![map3_2](https://user-images.githubusercontent.com/23075158/33822996-d2bd8668-de59-11e7-849a-313333f6d8bf.png)
