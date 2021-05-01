# Robotics (Python)

1. Path Planning (Bug1 and Bug2)
    - Brief introduction on the general concept of Motion Planning can be found [here](https://en.wikipedia.org/wiki/Motion_planning#:~:text=Motion%20planning%2C%20also%20path%20planning,animation%2C%20robotics%20and%20computer%20games.)
    - Bug1 and Bug2 are two of the most fundamental path planning algorithms in robotics.
    - Bug1
        - Bug1 is an exhaustive saerch algorithm, meaning the robot proceeds to find the goal after it completes circumnavigating the obstacles in the environment.
        - The robot fully circumnavigates the boundaries of the obstacles once and it finds the closest point to the next obstacle or the goal before it moves on. 
    - Bug2
        - Bug2 is a reinforced algorithm of Bug1. It still follows the boundaries of the obstacles to find the goal, yet there is one more concept added called "M-Line," which signifies the linear line that connects the start point directly to the goal.
        - Bug2 is "not" an exhaustive search since two distances, d_(reached) and d_(followed), inform the robot of the leave and arrive points on each obstacle.
        
3. Navigation (Generalized Voronoi Diagram Construction with Brushfire)
    - High level concept on GVD can be found [here](https://www.cs.columbia.edu/~pblaer/projects/path_planner/)

5. Non-Euclidean Probabilistic Roadmap 
6. Particle Filter Localization 
7. Learn and Predict Inverse Kinematics (Neural Network)
