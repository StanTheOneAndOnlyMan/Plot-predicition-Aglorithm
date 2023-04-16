import helpers.matplot_tools as mplt
import helpers.converter as conv
from helpers.graph import graph

import math
import random
import time

from collections import defaultdict
from simanneal import Annealer

import numpy as np

class TravellingSalesmanProblem(Annealer):

    """Test annealer with a travelling salesman problem.
    """

    # pass extra data (the distance matrix) into the constructor
    def __init__(self, state, distance_matrix):
        self.distance_matrix = distance_matrix
        super(TravellingSalesmanProblem, self).__init__(state)  # important!

    def move(self):
        """Swaps two cities in the route."""
        # no efficiency gain, just proof of concept
        # demonstrates returning the delta energy (optional)
        initial_energy = self.energy()

        a = random.randint(0, len(self.state) - 1)
        b = random.randint(0, len(self.state) - 1)
        self.state[a], self.state[b] = self.state[b], self.state[a]

        return self.energy() - initial_energy

    def energy(self):
        """Calculates the length of the route."""
        e = 0
        for i in range(len(self.state)):
            e += self.distance_matrix[self.state[i-1]][self.state[i]]
        return e

def main(input, obstacle):
    print("Anneal", time.time())
    start_time = time.time()
    corner_list = conv.format_input(input)
    coords = mplt.getRelevantCoords(corner_list, obstacle)

    init_state = list(coords)
    random.shuffle(init_state)

    distance_matrix = graph(coords)
    
    tsp = TravellingSalesmanProblem(init_state, distance_matrix)
    tsp.set_schedule(tsp.auto(minutes=0.2))
    # since our state is just a list, slice is the fastest way to copy
    tsp.copy_strategy = "slice"
    state, e = tsp.anneal()

    print(state)
    print("Route length: " + str(e))
    print("Time: " + str(time.time() - start_time))

    mplt.visualize_path(corner_list, state, obstacle)







    # distance_matrix = defaultdict(dict)
    # for xa, ya in coords.items():
    #     for xb, yb in coords.items():
    #         distance_matrix[xa][xb] = 0.0 if xb == xa else distance(ya, yb)
    


# def distance(a, b):
#     return math.sqrt(((a[0]-b[0])**2) + ((a[1]-b[1])**2))

# print(distance((1,6), (1,6)))

# def simulate(coords_dict):
#     distance_matrix = defaultdict(dict)
#     for xa, ya in coords_dict.items():
#         for xb, yb in coords_dict.items():
#             distance_matrix[xa][xb] = 0.0 if xb == xa else distance(ya, yb)

# coords = [{'id': 1, 'x': 0.270387, 'y': 0.295951}, {'id': 2, 'x': 0.0263765, 'y': 0.688287}, {'id': 3, 'x': 0.109928, 'y': 0.83403}, {'id': 4, 'x': 0.797513, 'y': 0.839556}, {'id': 5, 'x': 0.270387, 'y': 0.295951}]

# coords_dict = convert_input(coords)

# distance_matrix = defaultdict(dict)
# for xa, ya in coords_dict.items():
#     for xb, yb in coords_dict.items():
#         distance_matrix[xa][xb] = 0.0 if xb == xa else distance(ya, yb)
# print(distance_matrix)







# # initial state, a randomly-ordered itinerary
# init_state = list(coords)
# random.shuffle(init_state)

# # create a distance matrix
# distance_matrix = defaultdict(dict)
# for ka, va in coords.items():
#     for kb, vb in coords.items():
#         distance_matrix[ka][kb] = 0.0 if kb == ka else distance(va, vb)

# print(distance_matrix)

# def distance(a, b):
#     """Calculates distance between two latitude-longitude coordinates."""
#     R = 3963  # radius of Earth (miles)
#     lat1, lon1 = math.radians(a[0]), math.radians(a[1])
#     lat2, lon2 = math.radians(b[0]), math.radians(b[1])
#     return math.acos(math.sin(lat1) * math.sin(lat2) +
#                      math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2)) * R


# class TravellingSalesmanProblem(Annealer):

#     """Test annealer with a travelling salesman problem.
#     """

#     # pass extra data (the distance matrix) into the constructor
#     def __init__(self, state, distance_matrix):
#         self.distance_matrix = distance_matrix
#         super(TravellingSalesmanProblem, self).__init__(state)  # important!

#     def move(self):
#         """Swaps two cities in the route."""
#         # no efficiency gain, just proof of concept
#         # demonstrates returning the delta energy (optional)
#         initial_energy = self.energy()

#         a = random.randint(0, len(self.state) - 1)
#         b = random.randint(0, len(self.state) - 1)
#         self.state[a], self.state[b] = self.state[b], self.state[a]

#         return self.energy() - initial_energy

#     def energy(self):
#         """Calculates the length of the route."""
#         e = 0
#         for i in range(len(self.state)):
#             e += self.distance_matrix[self.state[i-1]][self.state[i]]
        # return e