from sympy import *
import numpy as np

def inverse_kinematics():

    J = [[-1.732, 2.598, 0],
         [-1    , 1.5  , 0],
         [0     , 0    , 1],
         [0     , -0.5 , 0],
         [0     , 0.866, 0],
         [1     ,     0, 0]]


    """
    J = [[-1.732, 2.598, 0],
         [-1, 1.5, 0],
         [0, 0, 1]]  
    """
    x, y, z, wx, wy, wz = symbols("x y z wx wy wz")

    xi = [1, 1, 1, 1, 1, 1]
    #xi = [1, y, 1]
    #xi = [1, 1, 1]


    J_T = np.transpose(J)

    J_TJ = np.matmul(J_T, J)

    J_in = np.linalg.inv(J_TJ)

    J_L = np.matmul(J_in, J_T)

    J_Lxi = np.matmul(J_L, xi)

    q_dot = np.transpose(J_Lxi)

    #print(q_dot)
    new_xi = np.matmul(J, q_dot)

    g_q = (1/2) * np.matmul(np.transpose(xi - np.matmul(J, q_dot)), (xi - np.matmul(J, q_dot)))
