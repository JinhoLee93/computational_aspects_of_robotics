# Path Planning (Bug1 and Bug2)

Written by Jinho Lee (jl5027@columbia.edu)

offline_bug2.py

**([Bug1](https://github.com/JinhoLee93/Robotics/blob/main/path_planning/bug1.png) and Bug2 algorithms are very similar. They only vary in a few lines of code. Thus, the focus here is Bug2.)**

- The robot travels from the start point to the goal via circumnavigating the circular obstacles. 

- def bug2()
    - Every bug algorithm in this case where every detail, such as coordinates, and the start and the end points, of the m-line and the obstacles is evident is extremely simple. 
    - One of the most important facets of Bug2 is the m-line which the robot follows along until it meets the goal. 
    - The m-line is defined as x axis
 - Since all the obstacles are spheres, the path can be easily defined if each hit and leave point is well found.
    - def is_hit() helps determine the points where the robot first hits each obstacles and, with the coordinates of the obstacles, the leave points can also be defined as easily. 
 - Navigation for Bug2 is more like brute force since the search itself is half exhaustive (circumnavigation) and half object-following (m-line).
    - Which way the robot takes when it's faced with each obstacle is totally [random](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html).
    - To calculate the correct path around the obstacles, [the quadratic equation](https://en.wikipedia.org/wiki/Quadratic_formula) and basic knowledge about geometric properties of sphere.
    
    - Everything is drawn with [Matplotlib](https://matplotlib.org/stable/index.html)
   
 - Finishes the path by reaching the goal from the last leave point.
 - Results show images like [this](https://github.com/JinhoLee93/Robotics/blob/main/path_planning/bug2.png)

Sphere_space_navigation.py
- The robot finds its goal based on two combined [potential functions](https://en.wikipedia.org/wiki/Scalar_potential) (Physics) of the spherical environment. 
- Can be understood with this magnificent gif from [potential functions page](https://en.wikipedia.org/wiki/Scalar_potential)
- ![](https://upload.wikimedia.org/wikipedia/commons/7/74/Gravity_field_near_earth.gif)
    - Attractive Potential
        - Intentionally gives the goal low potential so that the robot naturally falls in the goal.
    - Repulsive Potential 
        - Gives the obstacles high enough potential (here infinity) to push off the robot from the obstacles.
