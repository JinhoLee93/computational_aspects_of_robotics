# Navigation

Written by Jinho Lee (jl5027@columbia.edu)

brushfire.py
- Numbers signify the distance from a point and the obstacle from which the point is.
- Numbers increase from the obstacles including the boundaries of the environment like brushfire until they meet numbers from the other obstacles. 
- Illustrated below
- <img width="1152" alt="Screen Shot 2021-05-08 at 5 41 20 PM" src="https://user-images.githubusercontent.com/60580427/117532868-9fb9d780-b024-11eb-944d-18680d3c2346.png">
- And this will help define GVD (Generalized Voronoi Diagram) boundaries, such as below
- <img width="289" alt="p4 2_world1" src="https://user-images.githubusercontent.com/60580427/117532846-857ff980-b024-11eb-8a8b-63f85bd14aef.png">
- Pretty easily implemented with decisions.

gvd.py
- Essential plot functions were written by [Professor Tony Dear](https://www.engineering.columbia.edu/faculty/tony-dear)
- Creates GVD like the second image above. The results always vary by environment.
- Illustrated below are environments with different configurations.
- <img width="291" alt="p4 2_world3" src="https://user-images.githubusercontent.com/60580427/117533081-b876bd00-b025-11eb-9bcc-f503562216b2.png">
- <img width="296" alt="p4 2_world4" src="https://user-images.githubusercontent.com/60580427/117533085-ba408080-b025-11eb-850c-edb59fdd5d73.png">
