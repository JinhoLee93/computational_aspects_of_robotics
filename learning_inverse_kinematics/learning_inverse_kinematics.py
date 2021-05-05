# Written by Jinho Lee (jl5027@columbia.edu)

from sympy import *
import numpy as np
from numpy.linalg import matrix_rank
import math
import matplotlib.pyplot as plt
import sys
import random
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

def plot_loss(history):
  plt.plot(history.history['loss'], label='loss')
  plt.plot(history.history['val_loss'], label='val_loss')
  plt.xlabel('Epoch')
  plt.ylabel('Error [MPG]')
  plt.legend()
  plt.grid(True)
  plt.savefig('losses.png')



def dataset():
    configs = list()
    end_positions = list()

    for i in range(1000):
        t1 = random.random()*(2*np.pi) - np.pi
        t2 = random.random()*(2*np.pi) - np.pi
        d3 = random.random()*3
        FK = [[cos(t1) * cos(t2), -sin(t1), sin(t2) * cos(t1), -sin(t1) + d3 * sin(t2) * cos(t1)],
              [sin(t1) * cos(t2),  cos(t1), sin(t1) * sin(t2),  cos(t1) + d3 * sin(t1) * sin(t2)],
              [         -sin(t2),        0,           cos(t2),                      d3 * cos(t2)],
              [                0,        0,                 0,                                 1]]

        configs.append([t1, t2, d3])
        end_positions.append([FK[0][3], FK[1][3], FK[2][3]])

    configs = np.array(configs).astype(np.float32)
    end_positions = np.array(end_positions).astype(np.float32)

    return configs, end_positions



def model():
    model = keras.Sequential([
        layers.Dense(3),
        layers.Dense(50, activation='relu'),
        layers.Dense(3)
    ])

    model.compile(optimizer=tf.keras.optimizers.Adam(0.001),
                  loss=tf.keras.losses.MeanSquaredError())

    return model



def fit(m):
    configs, end_positions = dataset()

    history = m.fit(
        end_positions, configs,
        epochs=200,
        verbose=0,
        validation_split=0.2
    )
    plot_loss(history)

    return m



def predict(m):
    traj = np.zeros((100, 3))
    traj[:, 0] = -np.cos(np.linspace(0, 4 * np.pi, num=100)) ** 2
    traj[:, 1] = np.sin(np.linspace(0, 4 * np.pi, num=100)) ** 2
    traj[:, 2] = np.linspace(1, 2, num=100)

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(traj[:, 0], traj[:, 1], traj[:, 2])

    p = m.predict(traj)

    res = list()

    for i in range(100):
        t1 = p[i, 0]
        t2 = p[i, 1]
        d3 = p[i, 2]

        FK = [[cos(t1) * cos(t2), -sin(t1), sin(t2) * cos(t1), -sin(t1) + d3 * sin(t2) * cos(t1)],
              [sin(t1) * cos(t2),  cos(t1), sin(t1) * sin(t2),  cos(t1) + d3 * sin(t1) * sin(t2)],
              [         -sin(t2),        0,           cos(t2),                      d3 * cos(t2)],
              [                0,        0,                 0,                                 1]]

        res.append([FK[0][3], FK[1][3], FK[2][3]])

    res = np.array(res).astype(np.float32)
    ax.plot(res[:, 0], res[:, 1], res[:, 2])

    plt.show()
    plt.savefig('trajectories.png')


if __name__ == '__main__':
    m = model()
    predict(fit(m))
