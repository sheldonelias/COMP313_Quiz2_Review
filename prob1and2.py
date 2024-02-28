import matplotlib.pyplot as plt
import numpy as np

def prob1():
    plt.axis([-20, 130, 80, -20])

    plt.axis('on')
    plt.grid(True)

    x1 = 20
    x2 = 120
    y1 = 40
    y2 = 20

    dist = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    ux = (x2 - x1) / dist
    uy = (y2 - y1) / dist

    for p in np.arange(0, dist, .5):
        px = x1 + p * ux
        py = y1 + p * uy
        plt.scatter(px, py, s=1, color='g')

    plt.show()

    pass