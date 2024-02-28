import matplotlib.pyplot as plt
import numpy as np

def prob3(xc, yc):
    figure, axes = plt.subplots()
    axes.set_aspect(1)
    plt.grid(True)
    plt.axis([-10, 10, -10, 10])
    cx = 0
    cy = 0
    rad = 3

    p1 = 27 * np.pi / 180

    p2 = 269 * np.pi / 180

    dp = (p2 - p1) / 300

    for p in np.arange(p1, p2, dp):
        x = xc + rad * np.cos(p)
        y = yc + rad * np.sin(p)
        plt.scatter(x, y, s=1, color='k')

    plt.show()

    pass