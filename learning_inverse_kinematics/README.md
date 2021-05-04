# Learning Inverse Kinematics

forward_kinematics.py
- Lets the user easily calculate their robot's forward kinematics even with random variables
- All matrix calculations are arranged in accordance with [Denavit-Hartenberg Parameters](https://en.wikipedia.org/wiki/Denavit%E2%80%93Hartenberg_parameters)

inverse_kinematics.py
- Furthermore, the user is able to even calculate the [Jacobian matrix](https://en.wikipedia.org/wiki/Jacobian_matrix_and_determinant) for the angular and linear velocities of their robot's configuration.
- The user can choose either underconstrained or overconstrained manipulator configurations to calculate since they require different [pseudoinverse of the Jacobian](https://en.wikipedia.org/wiki/Moore%E2%80%93Penrose_inverse).
