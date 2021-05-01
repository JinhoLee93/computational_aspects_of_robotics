# Robotics under Professor [Tony Dear](https://www.engineering.columbia.edu/faculty/tony-dear) (Python)

1. Path Planning (Bug1 and Bug2)
    - Brief introduction on the general concept of Motion Planning can be found [here](https://en.wikipedia.org/wiki/Motion_planning#:~:text=Motion%20planning%2C%20also%20path%20planning,animation%2C%20robotics%20and%20computer%20games.)
    - Bug1 and Bug2 are two of the most fundamental path planning algorithms in robotics.
    - Bug1
        - Bug1 is an exhaustive saerch algorithm, meaning the robot proceeds to find the goal after it completes circumnavigating the obstacles in the environment.
        - The robot fully circumnavigates the boundaries of the obstacles once and it finds the closest point to the next obstacle or the goal before it moves on. 
    - Bug2
        - Bug2 is a reinforced algorithm of Bug1. It still follows the boundaries of the obstacles to find the goal, yet there is one more concept added called "M-Line," which signifies the linear line that connects the start point directly to the goal.
        - Bug2 is "not" an exhaustive search since two distances, d_(reached) and d_(followed), inform the robot of the leave and arrive points on each obstacle.
        
2. Navigation (Generalized Voronoi Diagram Construction with Brushfire)
    - High level concept on GVD can be found [here](https://www.cs.columbia.edu/~pblaer/projects/path_planner/)
    - GVD is constructed by brushfire (also called wavefront or grassfire) algorithm. This lets you easily find the collinding boundaries between the obstacles where GVD is drawn.
    - Use gradient ascent for the robot to reache the goal following the GVD.

3. Non-Euclidean Probabilistic Roadmap 
    - Brief introduction on the Probabilistic Roadmap can be found [here](http://www.cs.columbia.edu/~allen/F15/NOTES/Probabilisticpath.pdf)
4. Particle Filter Localization 
8. Learn and Predict Inverse Kinematics (Neural Network)
