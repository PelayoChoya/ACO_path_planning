#!/usr/bin/env python

from aco import Map
from aco import AntColony
import numpy as np
import sys
import argparse


def arguments_parsing():
    ''' Function used for handling the command line argument options '''
    parser = argparse.ArgumentParser()
    parser.add_argument('ants', help = 'the number of ants that made up the \
                        colony', type = int)
    parser.add_argument('iterations', help = 'the number of iterations to be \
                        perfomed by the algorithm', type = int)
    parser.add_argument('map', help = 'the map to calculate the path from', \
                        type = str)
    parser.add_argument('p', help = 'controls the amount of pheromone that is \
                        evaporated, range[0-1], precision 0.05', \
                        type = float, choices = \
                        np.around(np.arange(0.0,1.05,0.05),decimals = 2))
    parser.add_argument('Q', help = 'controls the amount of pheromone that is \
                        added', \
                        type = float)
    parser.add_argument('-d','--display', default = 0, action = 'count', \
                        help = 'display the map and the \
                        resulting path')
    args = parser.parse_args()
    return args.ants, args.iterations, args.map, args.p, args.Q, args.display

if __name__ == '__main__':
    ants, iterations, map_path, p, Q, display = arguments_parsing()
    # Get the map
    Map= Map(map_path)
    Colony = AntColony(Map, ants, iterations, p, Q)
    path = Colony.calculate_path()
    print path
    if display > 0:
        Map.represent_path(path)

