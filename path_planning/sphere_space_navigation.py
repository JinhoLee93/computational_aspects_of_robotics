# Jinho Lee (jl5027)
# Professor Tony Dear
# COMS4733 HW1 P4.2
# p4.2.py

#!/usr/bin/env python
import sys
import matplotlib.pyplot as plt
import numpy as np
import random
from scipy import optimize
from sympy import *

def plot(robot, input, goal):
    # Todo: Plot the c-space
    #fig = plt.figure()

    env_x = 0
    env_y = 0
    env_r = 10

    ax = plt.gca()

    ax.plot(env_x, env_y)
    ax.grid(True)
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')

    """
    # m-line plot
    start = [coordinates['start'][0], coordinates['goal'][0]]
    goal = [coordinates['start'][1], coordinates['goal'][1]]
    ax.plot(start, goal, '--', color='blue')
    """
    env = plt.Circle((env_x, env_y), env_r, color='k', fill=False)
    ax.add_patch(env)

    # Circles
    for i in range(len(input)):
        circle = plt.Circle(input[i][0], input[i][1], color='r')
        ax.add_patch(circle)

    # Graph limit
    ax.set_xlim((-10, 10))
    ax.set_ylim((-10, 10))

    # I added threshold to determine if the robot reaches the goal since
    # it seems like the gradient never gets to quite.
    threshold = 0.05
    step = 5
    x, y = symbols("x y")

    while True:
        g = [diff(phi(x, y, input), x).evalf(subs={x:robot[0], y:robot[1]}),
             diff(phi(x, y, input), y).evalf(subs={x:robot[0], y:robot[1]})]

        ax.plot(robot[0], robot[1], 'ko')

        robot = [robot[0] - (step * g[0]), robot[1] - (step * g[1])]

        if robot[0] > (9 - threshold) and robot[1] > (0 - threshold):
            break

    plt.savefig('4.2.png')

def distance(q, q1) -> float:

    return sqrt(((q[0] - q1[0]) ** 2) + ((q[1] - q1[1]) ** 2))

def phi(x, y, input, k=3):
    # Todo: Sphere navigation
    # q = current position coordinate
    # qgoal = goal coordinate
    # k = free variable (step size)

    beta = ((-distance([x, y], (0, 0)) ** 2) + (10 ** 2))
    for i in range(len(input)):
        beta *= ((distance([x, y], input[i][0]) ** 2) - (input[i][1] ** 2))

    return (distance([x, y], [9, 0]) ** 2) / \
           ((distance([x, y], [9, 0]) ** (2 * k)) + beta) ** (1 / k)

if __name__ == "__main__":

    coordinates = {'start': [-9, 0],
                   'goal': [9, 0]}

    #input = [((-5, 4), 2), ((1, -3), 2)]
    #input = [((-5, 4), 2), ((1, -3), 2), ((2.5, 5), 2)]
    # robot gets stuck in the local minimum but gets out of it when k = 3.
    input = [((-5, 4), 2), ((1, -3), 4), ((2.5, 5), 2)]

    robot = [-9, 0]

    plot(robot, input, coordinates['goal'])