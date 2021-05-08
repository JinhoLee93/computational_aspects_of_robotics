# Non Euclidean PRM

You can find the result [here](https://www.youtube.com/watch?v=k7dJsFfELGA&ab_channel=JinhoLee).

non_euclidean_prm.py
- **Scaffolding code gracefully taken from [the PythonRobotics project](https://pythonrobotics.readthedocs.io/en/latest/). Thus, Only two parts of the code has been written by Jinho Lee (jl5027@columbia.edu)**
- def sample_points()
  - Produces random points in free workspace between the start and the goal points. 
    - In order to do so, it needs collision detection because free workpace should not contain any obstacles.
    - Number of obstacles is specified at the beginning as OBSTACLES
  - Collision detection is done by detect_collision function provided.
  - Once the point is cleared of a hinderance, add it to the workpace.
  - Repeat this process for the determined number of samples (N_SAMPLE).
  
- def construct_prm()
  - Now we have sample points without collisions, it's time to connect them to create a PRM
  - There are two predetermined factors to account for while building the roadmap. They both greatly affect the performance of the algorithm.
    - N_KNN specifies number of neighbors around sample points. This will be used as one of the parameters of [NearestNeighbors](https://scikit-learn.org/stable/modules/neighbors.html).
    - MAX_EDGE_LEN specifies how long the connecting lines between the sample points should be. This will help the algorithm detect collisions between the connections and the obstacles.
    - Better the number and the length specified, better the results
  - Since the sample points were in a toroid workspace, the coordinates of the sample points must be converted into Euclidean so that they fit in the robot's C-Space.
  - Then it connects the points without collision detection.
  - Here, incremental collision detection is deployed so that every edge can be collision-free.
  - Then, it lets the edges be added to the C-Space. 
 
Sneak peek of the results
<img src="https://user-images.githubusercontent.com/60580427/117529081-7e4ef080-b010-11eb-81c0-5215e1a488ef.png" width="50%" height="50%">
