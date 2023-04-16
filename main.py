import algorithms.simulated_annealing.simanneal_implementation as simanneal
import algorithms.mlrose_library.mlrose_implementation as mlrose

corners = [{'x': 0.322044, 'y': 0.314627, 'id': 19}, {'x': 0.103846, 'y': 2.91517, 'id': 20}, {'x': 0.684124, 'y': 3.06918, 'id': 21}, {'x': 3.13889, 'y': 3.77642, 'id': 22}, {'x': 3.17714, 'y': 1.01072, 'id': 23}, {'x': 0.322044, 'y': 0.314627, 'id': 24}]
obstacle = True

def simanneal_calculation(corners, obstacle):
    simanneal.main(corners, obstacle)

def mlrose_calculation(corners, obstacle):
    mlrose.main(corners, obstacle)

if __name__ == "__main__":
    corners = [{'x': 193.508, 'y': 60.4366, 'id': 25}, {'x': 103.079, 'y': 230.786, 'id': 26}, {'x': 136.694, 'y': 337.136, 'id': 27}, {'x': 329.072, 'y': 306.006, 'id': 28}, {'x': 193.508, 'y': 60.4366, 'id': 29}]
    obstacle = False
    mlrose_calculation(corners, obstacle)