# Written by Jinho Lee (jl5027@columbia.edu)

#!/usr/bin/env python
import sys
import matplotlib.pyplot as plt
import numpy as np

def distance(q1, q2):
    return np.sqrt((q1[0] - q2[0]) ** 2 + (q1[1] - q2[1]) ** 2)

def setup(world):

    border = list()
    border_o = list()
    for i in range(len(world)):
        for j in range(len(world)):
            if i == 0 and j == 0:
                world[i][j] = 1
                border.append([i + 1, j + 1])
            elif i == 0 and j == len(world) - 1:
                world[i][j] = 1
                border.append([i + 1, j - 1])
            elif i == len(world) - 1 and j == 0:
                world[i][j] = 1
                border.append([i - 1, j + 1])
            elif i == len(world) - 1 and j == len(world) - 1:
                world[i][j] = 1
                border.append([i - 1, j - 1])
            elif i == 0:
                world[i][j] = 1
                border.append([i + 1, j])
            elif i == len(world) - 1:
                world[i][j] = 1
                border.append([i - 1, j])
            elif j == 0:
                world[i][j] = 1
                border.append([i, j + 1])
            elif j == len(world) - 1:
                world[i][j] = 1
                border.append([i, j - 1])

            elif world[i][j] > -1:
                if world[i][j-1] < 0:
                    world[i][j] = 1
                    border_o.append([i, j])
                elif world[i-1][j-1] < 0:
                    world[i][j] = 1
                    border_o.append([i, j])
                elif world[i-1][j] < 0:
                    world[i][j] = 1
                    border_o.append((i, j))
                elif world[i-1][j+1] < 0:
                    world[i][j] = 1
                    border_o.append([i, j])
                elif world[i+1][j-1] < 0:
                    world[i][j] = 1
                    border_o.append([i, j])
                elif world[i+1][j] < 0:
                    world[i][j] = 1
                    border_o.append([i, j])
                elif world[i][j+1] < 0:
                    world[i][j] = 1
                    border_o.append([i, j])
                elif world[i+1][j+1] < 0:
                    world[i][j] = 1
                    border_o.append([i, j])

    for i in range(len(border_o)):
        if world[border_o[i][0] + 1][border_o[i][1]] == 0:
            border.append([border_o[i][0] + 1, border_o[i][1]])
        if world[border_o[i][0] - 1][border_o[i][1]] == 0:
            border.append([border_o[i][0] - 1, border_o[i][1]])
        if world[border_o[i][0]][border_o[i][1] - 1] == 0:
            border.append([border_o[i][0], border_o[i][1] - 1])
        if world[border_o[i][0] + 1][border_o[i][1] + 1] == 0:
            border.append([border_o[i][0] + 1, border_o[i][1] + 1])
        if world[border_o[i][0] - 1][border_o[i][1] - 1] == 0:
            border.append([border_o[i][0] - 1, border_o[i][1] - 1])
        if world[border_o[i][0] + 1][border_o[i][1] - 1] == 0:
            border.append([border_o[i][0] + 1, border_o[i][1] - 1])
        if world[border_o[i][0] - 1][border_o[i][1] + 1] == 0:
            border.append([border_o[i][0] - 1, border_o[i][1] + 1])

    border_n = list()
    [border_n.append(v) for v in border if v not in border_n]

    return border_n

def get_border(world, iteration):
    border = list()
    for i in range(len(world)):
        for j in range(len(world)):
            if world[i][j] == iteration:
                if world[i - 1][j] == 0:
                    border.append([i - 1, j])
                if world[i + 1][j] == 0:
                    border.append([i + 1, j])
                if world[i][j - 1] == 0:
                    border.append([i, j - 1])
                if world[i][j + 1] == 0:
                    border.append([i, j + 1])
                if world[i - 1][j - 1] == 0:
                    border.append([i - 1, j - 1])
                if world[i - 1][j + 1] == 0:
                    border.append([i - 1, j + 1])
                if world[i + 1][j - 1] == 0:
                    border.append([i + 1, j - 1])
                if world[i + 1][j + 1] == 0:
                    border.append([i + 1, j + 1])

    border_n = list()
    [border_n.append(v) for v in border if v not in border_n]

    return border_n

def brushfire(world, border):
    iteration = 1
    while 0 in world:
        iteration += 1
        for i in range(len(border)):
            if world[border[i][0]][border[i][1]] == 0:
                world[border[i][0]][border[i][1]] = iteration
        border = get_border(world, iteration)

if __name__ == "__main__":
    world = np.loadtxt("./hw2/world4.txt")
    obstacles = list()

    border = setup(world)
    brushfire(world, border)

    np.savetxt('world.txt', world, fmt='%2.0f')
