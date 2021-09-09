# Learning Inverse Kinematics

Written by Jinho Lee (jl5027@columbia.edu)

[forward_kinematics.py](https://github.com/JinhoLee93/Robotics/blob/main/learning_inverse_kinematics/forward_kinematics.py)
- Lets the user easily calculate their robot's forward kinematics even with random variables.
- All matrix calculations are arranged in accordance with [Denavit-Hartenberg Parameters](https://en.wikipedia.org/wiki/Denavit%E2%80%93Hartenberg_parameters).

[inverse_kinematics.py](https://github.com/JinhoLee93/Robotics/blob/main/learning_inverse_kinematics/inverse_kinematics.py)
- Lets the user easily calculate their robot's inverse kinematics with their robot's angular and linear velocities that are calculated with forward_kinematics.py
- Furthermore, the user is able to even calculate the [Jacobian matrix](https://en.wikipedia.org/wiki/Jacobian_matrix_and_determinant) for the angular and linear velocities of their robot's configuration.
- The user can choose either underconstrained or overconstrained manipulator configurations to calculate according to the form of the Jacobian matrix since they require different [pseudoinverse of the Jacobian](https://en.wikipedia.org/wiki/Moore%E2%80%93Penrose_inverse).

[learning_inverse_kinematics.py](https://github.com/JinhoLee93/Robotics/blob/main/learning_inverse_kinematics/learning_inverse_kinematics.py)
- def dataset()
  - We're starting with creating 1000 random samples to train a neural network, using the given Forward Kinematics (FK).
  
- def model()
  - Creates [keras](https://www.tensorflow.org/api_docs/python/tf/keras/Sequential) model.
  - Uses input and output layers with 3 neurons for each variable (t1, t2, and d3) and one hidden layer.
  - Deploys the basic Adam optimizer and uses [MeanSquaredError()](https://www.tensorflow.org/api_docs/python/tf/keras/losses/MeanSquaredError).
  
- def fit()
  - Trains the network and plot the losses.
 
- def predict()
  - Calls [predict()](https://www.tensorflow.org/api_docs/python/tf/keras/Model#predict) and enters the results to the given FK.
  - Draws the trajectories of the losses.
