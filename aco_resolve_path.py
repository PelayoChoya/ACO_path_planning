#!/usr/bin/env python

from aco import Map
from aco import AntColony
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
    parser.add_argument('-d','--display', default = 0, action = 'count', \
                        help = 'display the map and the \
                        resulting path')
    args = parser.parse_args()
    return args.ants, args.iterations, args.map, args.display

if __name__ == '__main__':
    ants, iterations, map_path, display = arguments_parsing()
    # Get the map
    Map= Map(map_path)
    Colony = AntColony(Map, ants, iterations)
    path = Colony.calculate_path()
    print path
    if display > 0:
        Map.represent_path(path)

