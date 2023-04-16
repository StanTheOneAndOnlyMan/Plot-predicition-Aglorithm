from matplotlib.path import Path
import matplotlib.pyplot as plt
import matplotlib.patches as patches

import numpy as np
import itertools as it

# class Plot:
#     def __init__(self, corners):
#         codes = np.full(len(corners), Path.LINETO)
#         codes[0] = Path.MOVETO

#         self.path = Path(corners, codes)

#         grid = list(it.product(np.linspace(0, 1, 10),np.linspace(0, 1, 10)))
#         self.relevant_coords = list(filter(lambda x: (self.path.contains_point(x)), grid))


# newplot = Plot(corners=[[0.3649568, 0.14904938], [0.04430255, 0.35595042], [0.40504331, 0.61315582], [0.76140304, 0.74970297], [0.3649568, 0.14904938]])

# fig = plt.figure()
# ax = fig.add_subplot(111)
# patch = patches.PathPatch(newplot.path, facecolor='none')
# ax.add_patch(patch)
# ax.scatter(*zip(*newplot.relevant_coords), 3, color = "red")
# ax.set_xlim(0, 1)
# ax.set_ylim(0, 1)
# plt.show()

voertuig_breedte = 20

square_corners = np.array([[178,178],[178,222],[222,222],[222,178],[178,178]])

def square_path():
    codes = np.full(len(square_corners), Path.LINETO)
    codes[0] = Path.MOVETO
    return  Path(square_corners, codes)


def getRelevantCoords(corners, obstacle):
    codes = np.full(len(corners), Path.LINETO)
    codes[0] = Path.MOVETO

    path = Path(corners, codes)

    grid = list(it.product(np.linspace(0, 400, (400 / voertuig_breedte)),np.linspace(0, 400, (400 / voertuig_breedte))))

    coords = list(filter(lambda x: (path.contains_point(x)), grid))

    if obstacle:
        square_codes = np.full(len(square_corners), Path.LINETO)
        square_codes[0] = Path.MOVETO

        square_path = Path(square_corners, square_codes)
        square_coords = list(filter(lambda x: (square_path.contains_point(x)), grid))

        coords = [x for x in coords if x not in square_coords]

    return coords

def visualize_path(corners, list, obstacle):
    path_codes = np.full(len(list), Path.LINETO)
    path_codes[0] = Path.MOVETO

    corner_codes = np.full(len(corners), Path.LINETO)
    corner_codes[0] = Path.MOVETO

    path_path = Path(list, path_codes)
    corner_path = Path(corners, corner_codes)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    path_patch = patches.PathPatch(path_path, facecolor='none')
    corner_patch = patches.PathPatch(corner_path, facecolor='none')
    ax.add_patch(path_patch)
    ax.add_patch(corner_patch)

    if obstacle:
        square_patch = patches.PathPatch(square_path(), facecolor='none', edgecolor='red')
        ax.add_patch(square_patch)

    ax.scatter(*zip(*list), 3, color = "black")
    ax.set_xlim(0, 400)
    ax.set_ylim(0, 400)
    plt.show()