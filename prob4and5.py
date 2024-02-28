import matplotlib.pyplot as plt
import numpy as np

def prob4():
    x1 = -10
    x2 = 140
    y1 = 90
    y2 = -10
    plt.axis([x1, x2, y1, y2])

    plt.axis('on')
    plt.grid(True)

    x_vertices = [20, 30, 40, 20]
    y_vertices = [40, 20, 40, 40]
    plt.plot(x_vertices, y_vertices, color='k')
    plt.plot(x_vertices, y_vertices, color='k')
    plt.plot(x_vertices, y_vertices, color='k')

    # YOUR CODE GOES HERE

    plt.show()

    pass






''' For problem 5
dx = 10


for count in range(0, 100, 10):


    x_vertices = [x_val + dx for x_val in x_vertices]

    plt.plot(x_vertices, y_vertices, 'k')

'''