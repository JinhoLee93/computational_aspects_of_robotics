# Written by Jinho Lee (jl5027)

#!/usr/bin/env python
import sys
import matplotlib.pyplot as plt
import numpy as np
import random
def is_hit(obstacle, radius) -> bool:
    #Todo: Find out if the m-line intersects with the obstacle.
    hit = False
    if abs(obstacle[1]) < radius:
        hit = True

    return hit

def bug1(start, obstacles, goal):
    env_x = 0
    env_y = 0

    deg = np.pi / 180

    ax = plt.gca()

    ax.plot(env_x, env_y)
    ax.grid(True)
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')

    for i in range(len(obstacles)):
        circle = plt.Circle(obstacles[i][0], obstacles[i][1], color='r')
        ax.add_patch(circle)

    ax.plot(start[0], start[1], 'ko')
    ax.annotate("Start", (start[0], start[1]))
    ax.plot(goal[0], goal[1], 'ko')
    ax.annotate("Goal", (goal[0], goal[1]))

    # Show which obstacles are on the m-line.
    hit_obstacles = list()
    for i in range(len(obstacles)):
        if is_hit(obstacles[i][0], obstacles[i][1]):
            hit_obstacles.append(obstacles[i])

    # Sort the obstacles list by the hit order
    for i in range(len(hit_obstacles) - 1):
        if hit_obstacles[i][0][0] > hit_obstacles[i + 1][0][0]:
            t = hit_obstacles[i]
            hit_obstacles[i] = hit_obstacles[i + 1]
            hit_obstacles[i + 1] = t

    # Move the robot from the start point to the first hit point.
    r = hit_obstacles[0][1]
    x = hit_obstacles[0][0][0]
    y = hit_obstacles[0][0][1]

    a = 1
    b = -2 * x
    c = x ** 2 + y ** 2 - r ** 2

    q1 = ((-b) + np.sqrt((b ** 2 - (4 * a * c)))) / 2 * a
    q2 = ((-b) - np.sqrt((b ** 2 - (4 * a * c)))) / 2 * a

    if q1 < q2:
        hit = q1
        leave = q2
    else:
        hit = q2
        leave = q1

    while start[0] < hit:
        ax.plot(start[0], start[1], 'ko')
        start[0] += 0.1

    # Move the robot along the hit obstacles
    for i in range(len(hit_obstacles)):
        r = hit_obstacles[i][1]
        x = hit_obstacles[i][0][0]
        y = hit_obstacles[i][0][1]

        a = 1
        b = -2 * x
        c = x ** 2 + y ** 2 - r ** 2

        # hit and leave points
        q1 = ((-b) + np.sqrt((b ** 2 - (4 * a * c)))) / 2 * a
        q2 = ((-b) - np.sqrt((b ** 2 - (4 * a * c)))) / 2 * a

        ax.plot(q1, 0, 'ko')
        ax.plot(q2, 0, 'ko')

        if q1 < q2:
            hit = q1
            while leave < hit:
                ax.plot(leave, 0, 'ko')
                leave += 0.1
            leave = q2
        else:
            hit = q2
            while leave < hit:
                ax.plot(leave, 0, 'ko')
                leave += 0.1
            leave = q1
        # 0 = left, 1 = right
        dir = random.randint(0, 1)

        for i in range(1, 360):
            dx = (x) + (r * np.cos(i * deg))
            dy = (y) + (r * np.sin(i * deg))

            # (x, y) = (+, +)
            if x >= 0 and y >= 0:
                if dx < hit or dy > 0:  # (left)
                    ax.plot(dx, dy, 'ko')

            # (x, y) = (+, -)
            elif x >= 0 and y < 0:
                if dx > hit and dy > 0:  # (left)
                    ax.plot(dx, dy, 'ko')

            # (x, y) = (-, +)
            elif x < 0 and y >= 0:
                if dx < hit or dy > 0:  # (left)
                    ax.plot(dx, dy, 'ko')

            # (x, y) = (-, -)
            elif x < 0 and y < 0:
                if -dx < hit or dy > 0:  # (left)
                    ax.plot(dx, dy, 'ko')
                    # (x, y) = (+, +)

            if x >= 0 and y >= 0:
                if dx > hit and dy < 0:  # (right)
                    ax.plot(dx, dy, 'ko')

            # (x, y) = (+, -)
            elif x >= 0 and y < 0:
                if dx < hit or dy < 0:  # (right)
                    ax.plot(dx, dy, 'ko')

            # (x, y) = (-, +)
            elif x < 0 and y >= 0:
                if dx > hit and dy < 0:  # (right)
                    ax.plot(dx, dy, 'ko')

            # (x, y) = (-, -)
            elif x < 0 and y < 0:
                if -dx > hit and dy < 0:  # (right)
                    ax.plot(dx, dy, 'ko')

        # Robot moves according to the given direction
        if dir == 1:
            for i in range(1, 360):
                dx = (x) + (r * np.cos(i * deg))
                dy = (y) + (r * np.sin(i * deg))

                # (x, y) = (+, +)
                if x >= 0 and y >= 0:
                    if dx < hit or dy > 0:  # (left)
                        ax.plot(dx, dy, 'bo')

                # (x, y) = (+, -)
                elif x >= 0 and y < 0:
                    if dx > hit and dy > 0:  # (left)
                        ax.plot(dx, dy, 'bo')

                # (x, y) = (-, +)
                elif x < 0 and y >= 0:
                    if dx < hit or dy > 0:  # (left)
                        ax.plot(dx, dy, 'bo')

                # (x, y) = (-, -)
                elif x < 0 and y < 0:
                    if -dx < hit or dy > 0:  # (left)
                        ax.plot(dx, dy, 'bo')
        else:
            for i in range(1, 360):
                dx = (x) + (r * np.cos(i * deg))
                dy = (y) + (r * np.sin(i * deg))

                # (x, y) = (+, +)
                if x >= 0 and y >= 0:
                    if dx > hit and dy < 0:  # (right)
                        ax.plot(dx, dy, 'bo')

                # (x, y) = (+, -)
                elif x >= 0 and y < 0:
                    if dx < hit or dy < 0:  # (right)
                        ax.plot(dx, dy, 'bo')

                # (x, y) = (-, +)
                elif x < 0 and y >= 0:
                    if dx > hit and dy < 0:  # (right)
                        ax.plot(dx, dy, 'bo')

                # (x, y) = (-, -)
                elif x < 0 and y < 0:
                    if -dx > hit and dy < 0:  # (right)
                        ax.plot(dx, dy, 'bo')

    # Move the robot from the last leave point to the goal
    while leave < goal[0]:
        ax.plot(leave, goal[1], 'ko')
        leave += 0.1

    # Graph limit
    ax.set_xlim((-10, 10))
    ax.set_ylim((-10, 10))

    plt.savefig('bug1_final.png')

def bug2(start, obstacles, goal):
    env_x = 0
    env_y = 0

    deg = np.pi / 180

    ax = plt.gca()

    ax.plot(env_x, env_y)
    ax.grid(True)
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')

    for i in range(len(obstacles)):
        circle = plt.Circle(obstacles[i][0], obstacles[i][1], color='r')
        ax.add_patch(circle)

    ax.plot(start[0], start[1], 'ko')
    ax.annotate("Start", (start[0], start[1]))
    ax.plot(goal[0], goal[1], 'ko')
    ax.annotate("Goal", (goal[0], goal[1]))

    # Show which obstacles are on the m-line.
    hit_obstacles = list()
    for i in range(len(obstacles)):
        if is_hit(obstacles[i][0], obstacles[i][1]):
            hit_obstacles.append(obstacles[i])

    # Sort the obstacles list by the hit order
    for i in range(len(hit_obstacles)-1):
        if hit_obstacles[i][0][0] > hit_obstacles[i+1][0][0]:
            t = hit_obstacles[i]
            hit_obstacles[i] = hit_obstacles[i+1]
            hit_obstacles[i+1] = t

    # Move the robot from the start point to the first hit point.
    r = hit_obstacles[0][1]
    x = hit_obstacles[0][0][0]
    y = hit_obstacles[0][0][1]

    a = 1
    b = -2 * x
    c = x ** 2 + y ** 2 - r ** 2

    q1 = ((-b) + np.sqrt((b ** 2 - (4 * a * c)))) / 2 * a
    q2 = ((-b) - np.sqrt((b ** 2 - (4 * a * c)))) / 2 * a

    if q1 < q2:
        hit = q1
        leave = q2
    else:
        hit = q2
        leave = q1

    while start[0] < hit:
        ax.plot(start[0], start[1], 'ko')
        start[0] += 0.1

    # Move the robot along the hit obstacles
    for i in range(len(hit_obstacles)):
        r = hit_obstacles[i][1]
        x = hit_obstacles[i][0][0]
        y = hit_obstacles[i][0][1]

        a = 1
        b = -2 * x
        c = x ** 2 + y ** 2 - r ** 2

        # hit and leave points
        q1 = ((-b) + np.sqrt((b ** 2 - (4 * a * c)))) / 2 * a
        q2 = ((-b) - np.sqrt((b ** 2 - (4 * a * c)))) / 2 * a

        ax.plot(q1, 0, 'ko')
        ax.plot(q2, 0, 'ko')

        if q1 < q2:
            hit = q1
            while leave < hit:
                ax.plot(leave, 0, 'ko')
                leave += 0.1
            leave = q2
        else:
            hit = q2
            while leave < hit:
                ax.plot(leave, 0, 'ko')
                leave += 0.1
            leave = q1

        # 0 = left, 1 = right
        dir = random.randint(0, 1)

        # Robot moves according to the given direction
        if dir == 0:
            for i in range(1, 360):
                dx = (x) + (r * np.cos(i * deg))
                dy = (y) + (r * np.sin(i * deg))

                # (x, y) = (+, +)
                if x >= 0 and y >= 0:
                    if dx < hit or dy > 0: #(left)
                        ax.plot(dx, dy, 'ko')

                # (x, y) = (+, -)
                elif x >= 0 and y < 0:
                    if dx > hit and dy > 0: #(left)
                        ax.plot(dx, dy, 'ko')

                # (x, y) = (-, +)
                elif x < 0 and y >= 0:
                    if dx < hit or dy > 0: #(left)
                        ax.plot(dx, dy, 'ko')

                # (x, y) = (-, -)
                elif x < 0 and y < 0:
                    if -dx < hit or dy > 0: #(left)
                        ax.plot(dx, dy, 'ko')
        else:
            for i in range(1, 360):
                dx = (x) + (r * np.cos(i * deg))
                dy = (y) + (r * np.sin(i * deg))

                # (x, y) = (+, +)
                if x >= 0 and y >= 0:
                    if dx > hit and dy < 0:  # (right)
                        ax.plot(dx, dy, 'ko')

                # (x, y) = (+, -)
                elif x >= 0 and y < 0:
                    if dx < hit or dy < 0:  # (right)
                        ax.plot(dx, dy, 'ko')

                # (x, y) = (-, +)
                elif x < 0 and y >= 0:
                    if dx > hit and dy < 0:  # (right)
                        ax.plot(dx, dy, 'ko')

                # (x, y) = (-, -)
                elif x < 0 and y < 0:
                    if -dx > hit and dy < 0:  # (right)
                        ax.plot(dx, dy, 'ko')

    # Move the robot from the last leave point to the goal
    while leave < goal[0]:
        ax.plot(leave, goal[1], 'ko')
        leave += 0.1

    # Graph limit
    ax.set_xlim((-10, 10))
    ax.set_ylim((-10, 10))

    plt.savefig('bug2_final_p2.png')

if __name__ == "__main__":
    # Todo: Run Bug2

    coordinates = {'start': [-9, 0],
                   'goal': [9, 0]}

    # Three lists of obstacles
    #obstacles = [((-5, 3), 4), ((-2, -5), 3), ((5, -2), 4)]
    obstacles = [((3, -3), 3), ((-4, -1), 3)]
    #obstacles = [((-5, -3), 4), ((1, 2), 1), ((6, 1), 2)]

    #bug1(coordinates['start'], obstacles, coordinates['goal'])
    bug2(coordinates['start'], obstacles, coordinates['goal'])
