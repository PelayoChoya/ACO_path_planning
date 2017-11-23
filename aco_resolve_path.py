#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np

def read_map(map_name):
    ''' Reads data from an input map txt file'''
    map_planning = np.loadtxt('./maps/' + map_name, dtype = 'string')
    return map_planning

def parse_matrix(map_arr):
    ''' Takes the matrix and converts it
    into a float array '''
    map_arr[map_arr == 'O'] = 0
    map_arr[map_arr == 'E'] = 1
    map_arr[map_arr == 'S'] = 1
    map_arr[map_arr == 'F'] = 1

    return map_arr.astype(np.float)

def map_representation(map_arr):
    ''' Represents a map '''
    # Get Initial State and Final State's position
    initial_state = np.where(map_arr == 'S')
    final_state = np.where(map_arr == 'F')

    # Parse the matrix into 0 and 1s
    map_parsed = parse_matrix(map_arr)

    # Map representation
    plt.plot(initial_state[1],initial_state[0], 'ro', markersize=10)
    plt.plot(final_state[1],final_state[0], 'bo', markersize=10)
    plt.imshow(map_parsed, cmap='gray', interpolation = 'nearest')

    plt.show()

if __name__ == '__main__':
    # Get the map
    map_array = read_map('map1.txt')
    map_representation(map_array)
