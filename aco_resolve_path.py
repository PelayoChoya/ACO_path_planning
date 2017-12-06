#!/usr/bin/env python

from aco import Map
from aco import AntColony

if __name__ == '__main__':
    # Get the map
    Map= Map('map3.txt')
    Colony = AntColony(Map, 50, 25)
    path = Colony.calculate_path()
    print path
    Map.represent_path(path)


