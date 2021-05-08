# Computational Aspects of Robotics
Projects created by [Professor Tony Dear](https://www.engineering.columbia.edu/faculty/tony-dear) for Computational Aspects of Robotics

Written by Jinho Lee (jl5027@columbia.edu)

1. Path Planning (Bug1 and Bug2)
    - Brief introduction on the general concept of Motion Planning can be found [here](https://en.wikipedia.org/wiki/Motion_planning#:~:text=Motion%20planning%2C%20also%20path%20planning,animation%2C%20robotics%20and%20computer%20games.)
    - Bug1 and Bug2 are two of the most fundamental path planning algorithms in robotics.
    - Bug1
        - Bug1 is an exhaustive saerch algorithm, meaning the robot proceeds to find the goal after it completes circumnavigating the obstacles in the environment.
        - The robot fully circumnavigates the boundaries of the obstacles once and it finds the closest point to the next obstacle or the goal before it moves on. 
    - Bug2
        - Bug2 is a reinforced algorithm of Bug1. It still follows the boundaries of the obstacles to find the goal, yet there is one more concept added called "M-Line," which signifies the linear line that connects the start point directly to the goal.
        - Bug2 is "not" an exhaustive search since two distances, d_(reached) and d_(followed), inform the robot of the leave and arrive points on each obstacle.
        
2. Navigation (Generalized Voronoi Diagram (GVD) Construction with Brushfire)
    - High level concept on GVD can be found [here](https://www.cs.columbia.edu/~pblaer/projects/path_planner/)
    - GVD is constructed by brushfire (also called wavefront or grassfire) algorithm. This lets you easily find the collinding boundaries between the obstacles where GVD is drawn.
    - Use gradient ascent for the robot to reache the goal following the GVD.

3. Non-Euclidean Probabilistic Roadmap (PRM)
    - Brief introduction on the PRM can be found [here](http://www.cs.columbia.edu/~allen/F15/NOTES/Probabilisticpath.pdf) 
    - The scaffolding code was gracefully provided by [Professor Tony Dear](https://www.engineering.columbia.edu/faculty/tony-dear)
    - Just like most PRMs, the PRM here works as it samples the given number of sample points and connects them.
    - The connections between the sample points **must** not collide with any obstacles. Therefore, a collision detection algorithm was deployed.
    - As collision detection takes very significant part of the PRM, on what standard the PRM detects collisions must be taken into consideration. Here, [NeareastNeighbors](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html) is used so that each sample point is evaluated by the number of its neighbors in the vicinity. When a collision is detected, resample the points in it.
    - Since the arm is in a toroidal space, change its toroidal coordinate into Euclidean workspace coordinate.
    - You can find the result [here](https://www.youtube.com/watch?v=k7dJsFfELGA&ab_channel=JinhoLee)

4. Particle Filter Localization
    - Find the result [here](https://youtu.be/ENhtw4pTTxI)
    - High level description of Particle Filter can be found [here](https://en.wikipedia.org/wiki/Particle_filter) and that of Robotics Localization [here](https://en.wikipedia.org/wiki/Robot_navigation)
    - The skeleton code was inspired by [PythonRobotics](https://pythonrobotics.readthedocs.io/en/latest/modules/localization.html#particle-filter-localization) and written by [Professor Tony Dear](https://www.engineering.columbia.edu/faculty/tony-dear)
    - Filter mechanism is broken into three steps, which resemble neural networks.
        - Predict
            - This step is built around [Kalman Filter](https://en.wikipedia.org/wiki/Kalman_filter)
        - Update
            - Using the prediction already calculated and the information the robot receives from the landmarks around it. There is a huge spike on error meter at the beginning, but this behavior is expected since, first, the robot doesn't have any prior information about where it is, and, second, it the landmark information is highly limited.
        - Resample (Selective Process)
            - The samples are resampled only when the magnitude of the particle weights is small enough 
            - As suggested, resampling is done using [numpy.random.choice](https://numpy.org/doc/stable/reference/random/generated/numpy.random.choice.html).
    - As seen in the result video, the trajectory created by the filter keeps up with the robot pretty well though the result becomes much more accurate when there is more landmarks for the robot to receive more information from in the workspace. Thus, it is shown that the filter works perfectly when the robot goes right in between landmarks.
    
5. Learning Inverse Kinematics (Neural Network)
    - High level concept of Inverse Kinematics can be found [here](https://en.wikipedia.org/wiki/Inverse_kinematics)
    - In order to calculate the corret inverse kinematics of a robot, the robot's foward kinematics must be calculated first. 
        - Learn more about [Forward Kinematics](https://en.wikipedia.org/wiki/Forward_kinematics).
        - And I made this cool [program](https://github.com/JinhoLee93/Robotics/blob/main/learning_inverse_kinematics/forward_kinematics.py) that calculates forward kinematics for you and [this](https://github.com/JinhoLee93/Robotics/blob/main/learning_inverse_kinematics/inverse_kinematics.py) for inverse kinematics.
    - Steps
        - Prepare 1000 random samples to train a neural network with
        - Create a neural network using [Keras](https://www.tensorflow.org/tutorials/keras/regression#a_dnn_regression)
        - Predict the end effector position with the trained neural network.
    - A simple network with a basic optimizer would produce these [losses](https://github.com/JinhoLee93/Robotics/blob/main/learning_inverse_kinematics/losses.png) and this [trajectories](https://github.com/JinhoLee93/Robotics/blob/main/learning_inverse_kinematics/trajectories.png)
