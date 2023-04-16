import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose
import numpy as np

import time

from helpers.converter import format_input
import helpers.matplot_tools as mplt
from helpers.graph import graph

def main(input, obstacle):
    print("MLRose ", time.time())
    start_time = time.time()
    corner_list = format_input(input)
    coords = mplt.getRelevantCoords(corner_list, obstacle)

    problem_fit = mlrose.TSPOpt(length = len(coords), coords = coords, maximize = False)

    best_state, best_fitness = mlrose.genetic_alg(problem_fit, random_state=2, max_attempts=200, mutation_prob=0.5, pop_size=200)

    print(best_state)
    print("Route length: " + str(best_fitness))
    print("Time: " + str(time.time() - start_time))

    coords_ordered = []
    for number in best_state:
        coords_ordered.append(coords[number])
    mplt.visualize_path(corner_list, coords_ordered, obstacle)
    