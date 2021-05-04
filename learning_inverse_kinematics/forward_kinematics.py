from sympy import *
import numpy as np

def forward_kinematics():
    a1, al1, d1, t1 = symbols("a1 al1 d1 t1")
    a2, al2, d2, t2 = symbols("a2 al2 d2 t2")
    a3, al3, d3, t3 = symbols("a3 al3 d3 t3")
    a4, al4, d4, t4 = symbols("a4 al4 d4 t4")

    d1 = 10
    d2 = 0
    d4 = 0

    a1 = 0
    a2 = 4
    a3 = 2
    a4 = 5

    al1 = np.degrees(90)
    al2 = np.degrees(-90)
    al3 = np.degrees(90)

    print("Z0 = [0, 0, 1], O0 = [0, 0, 0]")
    # W.r.t x
    T11 = [[1,               0,                0, a1],
           [0, round(cos(al1)), round(-sin(al1)),  0],
           [0, round(sin(al1)),  round(cos(al1)),  0],
           [0,               0,                0,  1]]

    # z -> Do this first
    T12 = [[cos(t1), -sin(t1), 0,  0],
           [sin(t1),  cos(t1), 0,  0],
           [0      ,        0, 1,  d1],
           [0      ,        0, 0,  1]]

    T1 = np.matmul(T12, T11)
    #print("Z01 =", T1[:-1, 2], "O01 =", T1[:-1, 3])
    print("T01 =", T1)


    T21 = [[1,               0,                0, a2],
           [0, round(cos(al2)), round(-sin(al2)),  0],
           [0, round(sin(al2)),  round(cos(al2)),  0],
           [0,               0,                0,  1]]

    T22 = [[cos(t2), -sin(t2), 0,  0],
           [sin(t2),  cos(t2), 0,  0],
           [0      ,        0, 1, d2],
           [0      ,        0, 0,  1]]

    T2 = np.matmul(T22, T21)
    #print("Z02 =", T2[:-1, 2], "O02 =", T2[:-1, 3])
    print("T12 =", T2)

    T31 = [[1,               0,                0, a3],
           [0, round(cos(al3)), round(-sin(al3)),  0],
           [0, round(sin(al3)),  round(cos(al3)),  0],
           [0,               0,                0,  1]]

    # wrt z
    T32 =  [[1, 0, 0,      0],
            [0, 1, 0,      0],
            [0, 0, 1, d3 + 1],
            [0, 0, 0,      1]]

    T3 = np.matmul(T32, T31)
    #print("Z03 =", T3[:-1, 2], "O03 =", T3[:-1, 3])
    print("T23 =", T3)

    T41 = [[      1,        0, 0,  a4],
           [      0,        1, 0,   0],
           [      0,        0, 1,   0],
           [      0,        0, 0,   1]]

    T42 = [[cos(t4), -sin(t4), 0,  0],
           [sin(t4),  cos(t4), 0,  0],
           [      0,        0, 1, d4],
           [      0,        0, 0,  1]]

    T4 = np.matmul(T42, T41)

    T04 = np.matmul(np.matmul(np.matmul(T1, T2), T3), T4)
    #print("O04 = ", T4[:-1, 3])
    print("T34 =", T04)

    #print(T04)
