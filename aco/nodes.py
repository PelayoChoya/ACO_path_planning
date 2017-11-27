#!/usr/bin/env python

class Nodes:
    ''' Class for representing the nodes
        used by the ACO algorithm '''
    def __init__(self, row, col, spec):
        self.row = row
        self.col = col
        self.spec = spec

    def set_pheromone_level(self, pheromone):
        ''' Sets the pheromone level
            for the node '''
        self.pheromone = pheromone

    def get_pheromone_level(self):
        ''' Returns the pheromone level
            of the node '''
        return self.pheromone

    def get_indexes(self):
        ''' Returns indexes of the node '''
        return (self.row, self.col)

    def get_type(self):
        ''' Returns the node's type '''
        return self.spec

    def is_empty(self):
        ''' Returns 1 if the Node is empty '''
        if self.spec in ('E','S','F'):
            return 1
        else:
            return 0
