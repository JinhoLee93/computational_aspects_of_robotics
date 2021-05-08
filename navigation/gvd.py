# Jinho Lee (jl5027)
# Professor Tony Dear
# COMS4733 HW2 P4.2
# gvd.py

#!/usr/bin/env python
import sys
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

def distance(q1, q2):
    return np.sqrt((q1[0] - q2[0]) ** 2 + (q1[1] - q2[1]) ** 2)


def setup(world, pointers):
    border = list()
    border_o = list()
    for i in range(len(world)):
        for j in range(len(world)):
            if i == 0 and j == 0:
                world[i][j] += 1
                pointers[(i, j)] = (float("inf"), float("inf"))

            elif i == 0 and j == len(world) - 1:
                world[i][j] = 1
                pointers[(i, j)] = (float("inf"), float("inf"))

            elif i == len(world) - 1 and j == 0:
                world[i][j] = 1
                pointers[(i, j)] = (float("inf"), float("inf"))

            elif i == len(world) - 1 and j == len(world) - 1:
                world[i][j] = 1
                pointers[(i, j)] = (float("inf"), float("inf"))

            elif i == 0:
                world[i][j] = 1
                pointers[(i, j)] = (i, float("inf"))
                if pointers[(i + 1, j)] == 0 or pointers[(i + 1, j)] == pointers[(i, j)]:
                    border.append([i + 1, j])
                    pointers[(i + 1, j)] = pointers[(i, j)]
                """else:
                    pointers[(i + 1, j)] = (float("inf"), float("inf"))"""

            elif i == len(world) - 1:
                world[i][j] = 1
                pointers[(i, j)] = (i, float("inf"))
                if pointers[(i - 1, j)] == 0 or pointers[(i - 1, j)] == pointers[(i, j)]:
                    border.append([i - 1, j])
                    pointers[(i - 1, j)] = pointers[(i, j)]
                """else:
                    pointers[(i - 1, j)] = (float("inf"), float("inf"))"""

            elif j == 0:
                world[i][j] = 1
                pointers[(i, j)] = (float("inf"), j)
                if pointers[(i, j + 1)] == 0 or pointers[(i, j + 1)] == pointers[(i, j)]:
                    border.append([i, j + 1])
                    pointers[(i, j + 1)] = pointers[(i, j)]
                """else:
                    pointers[(i, j + 1)] = (float("inf"), float("inf"))"""

            elif j == len(world) - 1:
                world[i][j] = 1
                pointers[(i, j)] = (float("inf"), j)
                if pointers[(i, j - 1)] == 0 or pointers[(i, j - 1)] == pointers[(i, j)]:
                    border.append([i, j - 1])
                    pointers[(i, j - 1)] = pointers[(i, j)]
                """else:
                    pointers[(i, j - 1)] = (float("inf"), float("inf"))"""

            # obstacle boundary
            elif world[i][j] > -1:
                if world[i][j - 1] < 0:
                    world[i][j] = 1
                    border_o.append([i, j])
                    pointers[(i, j)] = (world[i][j - 1], world[i][j - 1])

                if world[i - 1][j - 1] < 0:
                    world[i][j] = 1
                    border_o.append([i, j])
                    pointers[(i, j)] = (world[i - 1][j - 1], world[i - 1][j - 1])

                if world[i - 1][j] < 0:
                    world[i][j] = 1
                    border_o.append([i, j])
                    pointers[(i, j)] = (world[i - 1][j], world[i - 1][j])

                if world[i - 1][j + 1] < 0:
                    world[i][j] = 1
                    border_o.append([i, j])
                    pointers[(i, j)] = (world[i - 1][j + 1], world[i - 1][j + 1])

                if world[i + 1][j - 1] < 0:
                    world[i][j] = 1
                    border_o.append([i, j])
                    pointers[(i, j)] = (world[i + 1][j - 1], world[i + 1][j - 1])

                if world[i + 1][j] < 0:
                    world[i][j] = 1
                    border_o.append([i, j])
                    pointers[(i, j)] = (world[i + 1][j], world[i + 1][j])

                if world[i][j + 1] < 0:
                    world[i][j] = 1
                    border_o.append([i, j])
                    pointers[(i, j)] = (world[i][j + 1], world[i][j + 1])

                if world[i + 1][j + 1] < 0:
                    world[i][j] = 1
                    border_o.append([i, j])
                    pointers[(i, j)] = (world[i + 1][j + 1], world[i + 1][j + 1])

            if world[i][j] < 0:
                pointers[(i, j)] = (world[i][j], world[i][j])

    for i in range(len(border_o)):
        if world[border_o[i][0] + 1][border_o[i][1]] == 0:
            border.append([border_o[i][0] + 1, border_o[i][1]])
            pointers[(border_o[i][0] + 1, border_o[i][1])] = pointers[(border_o[i][0], border_o[i][1])]

        if world[border_o[i][0] - 1][border_o[i][1]] == 0:
            border.append([border_o[i][0] - 1, border_o[i][1]])
            pointers[(border_o[i][0] - 1, border_o[i][1])] = pointers[(border_o[i][0], border_o[i][1])]

        if world[border_o[i][0]][border_o[i][1] - 1] == 0:
            border.append([border_o[i][0], border_o[i][1] - 1])
            pointers[(border_o[i][0], border_o[i][1] - 1)] = pointers[(border_o[i][0], border_o[i][1])]

        if world[border_o[i][0] + 1][border_o[i][1] + 1] == 0:
            border.append([border_o[i][0] + 1, border_o[i][1] + 1])
            pointers[(border_o[i][0] + 1, border_o[i][1] + 1)] = pointers[(border_o[i][0], border_o[i][1])]

        if world[border_o[i][0] - 1][border_o[i][1] - 1] == 0:
            border.append([border_o[i][0] - 1, border_o[i][1] - 1])
            pointers[(border_o[i][0] - 1, border_o[i][1] - 1)] = pointers[(border_o[i][0], border_o[i][1])]

        if world[border_o[i][0] + 1][border_o[i][1] - 1] == 0:
            border.append([border_o[i][0] + 1, border_o[i][1] - 1])
            pointers[(border_o[i][0] + 1, border_o[i][1] - 1)] = pointers[(border_o[i][0], border_o[i][1])]

        if world[border_o[i][0] - 1][border_o[i][1] + 1] == 0:
            border.append([border_o[i][0] - 1, border_o[i][1] + 1])
            pointers[(border_o[i][0] - 1, border_o[i][1] + 1)] = pointers[(border_o[i][0], border_o[i][1])]

    border_n = list()
    [border_n.append(v) for v in border if v not in border_n]

    return border_n


def get_border(world, iteration, pointers):
    border = list()
    for i in range(len(world)):
        for j in range(len(world)):
            if world[i][j] == iteration:
                if world[i - 1][j] == 0:
                    if pointers[(i - 1, j)] == 0 or pointers[(i - 1, j)] == pointers[(i, j)]:
                        pointers[(i - 1, j)] = pointers[(i, j)]
                        border.append([i - 1, j])
                    else:
                        pointers[(i - 1, j)] = (float("inf"), float("inf"))

                if world[i + 1][j] == 0:
                    if pointers[(i + 1, j)] == 0 or pointers[(i + 1, j)] == pointers[(i, j)]:
                        pointers[(i + 1, j)] = pointers[(i, j)]
                        border.append([i + 1, j])
                    else:
                        pointers[(i + 1, j)] = (float("inf"), float("inf"))

                if world[i][j - 1] == 0:
                    if pointers[(i, j - 1)] == 0 or pointers[(i, j - 1)] == pointers[(i, j)]:
                        pointers[(i, j - 1)] = pointers[(i, j)]
                        border.append([i, j - 1])
                    else:
                        pointers[(i, j - 1)] = (float("inf"), float("inf"))

                if world[i][j + 1] == 0:
                    if pointers[(i, j + 1)] == 0 or pointers[(i, j + 1)] == pointers[(i, j)]:
                        pointers[(i, j + 1)] = pointers[(i, j)]
                        border.append([i, j + 1])
                    else:
                        pointers[(i, j + 1)] = (float("inf"), float("inf"))

                if world[i - 1][j - 1] == 0:
                    if pointers[(i - 1, j - 1)] == 0 or pointers[(i - 1, j - 1)] == pointers[(i, j)]:
                        pointers[(i - 1, j - 1)] = pointers[(i, j)]
                        border.append([i - 1, j - 1])
                    else:
                        pointers[(i - 1, j - 1)] = (float("inf"), float("inf"))

                if world[i - 1][j + 1] == 0:
                    if pointers[(i - 1, j + 1)] == 0 or pointers[(i - 1, j + 1)] == pointers[(i, j)]:
                        pointers[(i - 1, j + 1)] = pointers[(i, j)]
                        border.append([i - 1, j + 1])
                    else:
                        pointers[(i - 1, j + 1)] = (float("inf"), float("inf"))

                if world[i + 1][j - 1] == 0:
                    if pointers[(i + 1, j - 1)] == 0 or pointers[(i + 1, j - 1)] == pointers[(i, j)]:
                        pointers[(i + 1, j - 1)] = pointers[(i, j)]
                        border.append([i + 1, j - 1])
                    else:
                        pointers[(i + 1, j - 1)] = (float("inf"), float("inf"))

                if world[i + 1][j + 1] == 0:
                    if pointers[(i + 1, j + 1)] == 0 or pointers[(i + 1, j + 1)] == pointers[(i, j)]:
                        pointers[(i + 1, j + 1)] = pointers[(i, j)]
                        border.append([i + 1, j + 1])
                    else:
                        pointers[(i + 1, j + 1)] = (float("inf"), float("inf"))

    border_n = list()
    [border_n.append(v) for v in border if v not in border_n]

    return border_n


def brushfire(world, border, pointers):
    iteration = 1
    while 0 in world:
        iteration += 1
        for i in range(len(border)):
            if world[border[i][0]][border[i][1]] == 0:
                world[border[i][0]][border[i][1]] = iteration
                if world[border[i][0] - 1][border[i][1]] > 0:
                    if pointers[(border[i][0] - 1, border[i][1])] != pointers[(border[i][0], border[i][1])]:
                        pointers[(border[i][0] - 1, border[i][1])] = (float("inf"), float("inf"))
                if world[border[i][0] + 1][border[i][1]] > 0:
                    if pointers[(border[i][0] + 1, border[i][1])] != pointers[(border[i][0], border[i][1])]:
                        pointers[(border[i][0] + 1, border[i][1])] = (float("inf"), float("inf"))
                if world[border[i][0]][border[i][1] - 1] > 0:
                    if pointers[(border[i][0], border[i][1] - 1)] != pointers[(border[i][0], border[i][1])]:
                        pointers[(border[i][0], border[i][1] - 1)] = (float("inf"), float("inf"))
                if world[border[i][0]][border[i][1] + 1] > 0:
                    if pointers[(border[i][0], border[i][1] + 1)] != pointers[(border[i][0], border[i][1])]:
                        pointers[(border[i][0], border[i][1] + 1)] = (float("inf"), float("inf"))
                if world[border[i][0] - 1][border[i][1] - 1] > 0:
                    if pointers[(border[i][0] - 1, border[i][1] - 1)] != pointers[(border[i][0], border[i][1])]:
                        pointers[(border[i][0] - 1, border[i][1] - 1)] = (float("inf"), float("inf"))
                if world[border[i][0] - 1][border[i][1] + 1] > 0:
                    if pointers[(border[i][0] - 1, border[i][1] + 1)] != pointers[(border[i][0], border[i][1])]:
                        pointers[(border[i][0] - 1, border[i][1] + 1)] = (float("inf"), float("inf"))
                if world[border[i][0] + 1][border[i][1] - 1] > 0:
                    if pointers[(border[i][0] + 1, border[i][1] - 1)] != pointers[(border[i][0], border[i][1])]:
                        pointers[(border[i][0] + 1, border[i][1] - 1)] = (float("inf"), float("inf"))
                if world[border[i][0] + 1][border[i][1] + 1] > 0:
                    if pointers[(border[i][0] + 1, border[i][1] + 1)] != pointers[(border[i][0], border[i][1])]:
                        pointers[(border[i][0] + 1, border[i][1] + 1)] = (float("inf"), float("inf"))

        border = get_border(world, iteration, pointers)


def plot_GVD(grid, GVD, path=None):
    fig, ax = plt.subplots()
    GVD_grid = np.copy(grid)
    GVD_x, GVD_y = zip(*GVD)
    GVD_grid[GVD_x, GVD_y] = 20

    img1 = ax.imshow(GVD_grid, cmap="RdBu", alpha=0.6)
    obstacles = GVD_grid.copy()
    obstacles[obstacles < 0] = -2.0
    masked_data = np.ma.masked_where(obstacles > 0, obstacles)
    img2 = ax.imshow(masked_data, cmap="bwr")
    legend_elements = [Patch(facecolor='blue', label='Obstacle'),
                       Patch(facecolor='#83b1d3', label='GVD')]
    if path:
        path_x, path_y = zip(*path)
        GVD_grid[path_x, path_y] = 40.0
        grid_path = GVD_grid.copy()
        grid_path = np.ma.masked_where(grid_path != 40.0, grid_path)
        img3 = ax.imshow(grid_path, cmap="cool_r", interpolation="nearest")
        legend_elements.append(Patch(facecolor='#e741f6', label='path'))

    ax.legend(handles=legend_elements)
    plt.show()


if __name__ == "__main__":
    world = np.loadtxt("./HW2/world1.txt")
    obstacles = list()
    pointers = dict()
    for i in range(len(world)):
        for j in range(len(world)):
            pointers[(i, j)] = 0

    border = setup(world, pointers)
    brushfire(world, border, pointers)
    gvd = list()
    for i in pointers.keys():
        if pointers[i] == (float("inf"), float("inf")):
            gvd.append(i)

    plot_GVD(world, gvd)
