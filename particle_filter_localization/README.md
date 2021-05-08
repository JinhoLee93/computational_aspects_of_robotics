# Particle Filter Localization

Written by Jinho Lee (jl5027@columbia.edu)

particle_filter_localization.py
- For this project, only parts that I had to finish were
  - def predict()
    - Predicts the robot's range and bearing to the landmarks
    - Based on particle motion model with Gaussian mean noise

  - def update()
    - Updates the robot's likelihood weight using the robot's predicted range and bearing

  - def resample()
    - Particles get resampled by [numpy.random.choice](https://numpy.org/doc/stable/reference/random/generated/numpy.random.choice.html) 

localzation.png
- Shows how well the particles converge to the actual robot path.

errors.png
- Each graph represents an error that occurs during the particles' convergence.
- You can find why y error spikes at the beginning [here](https://github.com/JinhoLee93/Robotics/blob/main/README.md)

[Result](https://youtu.be/ENhtw4pTTxI)

Sneak Peek at the Result
<img src="https://user-images.githubusercontent.com/60580427/117530725-c1fa2800-b019-11eb-8aa2-23fc2c9e17b6.png" width="50%" height="50%">
