#!/usr/bin/env python

from aco import Map
from aco import AntColony

if __name__ == '__main__':
    # Get the map
    Map= Map('map1.txt')
    Colony = AntColony(Map, 50, 20)
    print Colony.calculate_path()

