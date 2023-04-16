from collections import defaultdict
import math

def distance(a, b):
    return math.sqrt(((a[0]-b[0])**2) + ((a[1]-b[1])**2))

def graph(coordinates):
    distance_matrix = defaultdict(dict)
    for c1 in coordinates:
        for c2 in coordinates:
            distance_matrix[c1][c2] = 0.0 if c2 == c1 else distance(c1, c2)

    return distance_matrix
    