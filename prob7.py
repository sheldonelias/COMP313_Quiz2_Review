import matplotlib.pyplot as plt
import numpy as np

def prob7():
    figure, axes = plt.subplots()
    axes.set_aspect(1)
    box_edge_length = 5
    xc_start = 0
    xc_end = 50
    yc_start = 20
    yc_end = 50
    dx = 10

    x1 = xc_start - 10
    x2 = xc_end + 10
    y1 = -range(xc_end)[-1] - 10
    y2 = yc_end + 10
    plt.axis([x1, x2, y1, y2])

    plt.axis('on')
    plt.grid(True)

    for x_val in np.arange(0, xc_end, dx):
        x_vertices = [x_val, x_val, x_val + box_edge_length, x_val + \
                      box_edge_length, x_val]
        y_vertices = [yc_start, yc_start - box_edge_length, yc_start - \
                      box_edge_length, yc_start, yc_start]

        print('x_vals:', x_vertices)
        print('y_vals:', y_vertices)
        plt.plot(x_vertices, y_vertices, 'b')

    plt.show()

    pass