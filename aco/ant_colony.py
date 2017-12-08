#!/usr/bin/env python

import numpy as np

class AntColony:
    ''' Class used for handling
        the behaviour of the whole
        ant colony '''
    class Ant:
        ''' Class used for handling
            the ant's
            individual behaviour '''
        def __init__(self, start_node_pos, final_node_pos):
            self.start_pos = start_node_pos
            self.actual_node= start_node_pos
            self.final_node = final_node_pos
            self.visited_nodes = []
            self.final_node_reached = False
            self.remember_visited_node(start_node_pos)

        def move_ant(self, node_to_visit):
            ''' Moves ant to the selected node '''
            self.actual_node = node_to_visit
            self.remember_visited_node(node_to_visit)

        def remember_visited_node(self, node_pos):
            ''' Appends the visited node to
                the list of visited nodes '''
            self.visited_nodes.append(node_pos)

        def get_visited_nodes(self):
            ''' Returns the list of
                visited nodes '''
            return self.visited_nodes

        def is_final_node_reached(self):
            ''' Checks if the ant has reached the
                final destination '''
            if self.actual_node == self.final_node :
                self.final_node_reached = True

        def enable_start_new_path(self):
            ''' Enables a new path search setting
                the final_node_reached variable to
                false '''
            self.final_node_reached = False

        def setup_ant(self):
            ''' Clears the list of visited nodes
                it stores the first one
                and selects the first one as initial'''
            self.visited_nodes[1:] =[]
            self.actual_node= self.start_pos

    def __init__(self, in_map, no_ants, iterations, evaporation_factor,
                 pheromone_adding_constant):
        self.map = in_map
        self.no_ants = no_ants
        self.iterations = iterations
        self.evaporation_factor = evaporation_factor
        self.pheromone_adding_constant = pheromone_adding_constant
        self.paths = []
        self.ants = self.create_ants()
        self.best_result = []

    def create_ants(self):
        ''' Creates a list containin the
            total number of ants specified
            in the initial node '''
        ants = []
        for i in range(self.no_ants):
            ants.append(self.Ant(self.map.initial_node, self.map.final_node))
        return ants

    def select_next_node(self, actual_node):
        ''' Randomly selects the next node
            to visit '''

        # Compute the total sumatory of the pheromone of each edge
        total_sum = 0.0
        for edge in actual_node.edges:
            total_sum += edge['Pheromone']

        # Calculate probability of each edge
        prob = 0
        edges_list = []
        p = []
        for edge in actual_node.edges:
            prob = edge['Pheromone']/total_sum
            edge['Probability'] = prob
            edges_list.append(edge)
            p.append(prob)

        # Clear probability values
        for edge in actual_node.edges:
            edge['Probability'] = 0.0

        # Return the node based on the probability of the solutions
        return np.random.choice(edges_list,1, p)[0]['FinalNode']

    def pheromone_update(self):
        ''' Updates the pheromone level
            of the each of the trails
            and sorts the paths by lenght '''
        # Sort the list according to the size of the lists
        self.sort_paths()
        for i, path in enumerate(self.paths):
            for j, element in enumerate(path):
                for edge in self.map.nodes_array[element[0]][element[1]].edges:
                    if (j+1) < len(path):
                        if edge['FinalNode'] == path[j+1]:
                            edge['Pheromone'] = (1.0 -
                                                 self.evaporation_factor) * \
                            edge['Pheromone'] + \
                            self.pheromone_adding_constant/float(len(path))
                        else:
                            edge['Pheromone'] = (1.0 -
                                                 self.evaporation_factor) * edge['Pheromone']
    def empty_paths(self):
        ''' Empty the list of paths '''
        self.paths[:]

    def sort_paths(self):
        ''' Sorts the paths '''
        self.paths.sort(key=len)

    def add_to_path_results(self, in_path):
        ''' Appends the path to
            the results path list'''
        self.paths.append(in_path)

    def get_coincidence_indices(self,lst, element):
        ''' Gets the indices of the coincidences
            of elements in the path '''
        result = []
        offset = -1
        while True:
            try:
                offset = lst.index(element, offset+1)
            except ValueError:
                return result
            result.append(offset)

    def delete_loops(self, in_path):
        ''' Checks if there is a loop in the
            resulting path and deletes it '''
        res_path = list(in_path)
        for element in res_path:
            coincidences = self.get_coincidence_indices(res_path, element)
            # reverse de list to delete elements from back to front of the list
            coincidences.reverse()
            for i,coincidence in enumerate(coincidences):
                if not i == len(coincidences)-1:
                    res_path[coincidences[i+1]:coincidence] = []

        return res_path

    def calculate_path(self):
        ''' Carries out the process to
            get the best path '''
        # Repeat the cicle for the specified no of times
        for i in range(self.iterations):
            for ant in self.ants:
                ant.setup_ant()
                while not ant.final_node_reached:
                    # Randomly selection of the node to visit
                    node_to_visit = self.select_next_node(self.map.nodes_array[int(ant.actual_node[0])][int(ant.actual_node[1])])

                    # Move ant to the next node randomly selected
                    ant.move_ant(node_to_visit)

                    # Check if solution has been reached
                    ant.is_final_node_reached()

                # Add the resulting path to the path list
                self.add_to_path_results(self.delete_loops(ant.get_visited_nodes()))

                # Enable the ant for a new search
                ant.enable_start_new_path()

            # Update the global pheromone level
            self.pheromone_update()
            self.best_result = self.paths[0]
            # Empty the list of paths
            self.empty_paths()
            print  'Iteration: ',i, ' lenght of the path: ', len(self.best_result)
        return self.best_result
