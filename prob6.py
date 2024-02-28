import matplotlib.pyplot as plt
import numpy as np


def prob6_sol1(xc, yc, xp, yp, rz):
    # Numpy solution with comments
    # Set up array with trig functions with rotation angle arg
    trig_array = np.array([[np.cos(rz), -np.sin(rz)], [np.sin(rz), np.cos(rz)]])
    print('trig_array')
    print(trig_array)
    print('local_point_array')

    # Set up array with local points
    local_point_array = np.array([xp, yp])
    print(local_point_array)
    print('center_point_array')

    # Set up array with center coords
    center_point_array = np.array([xc, yc])
    print(center_point_array)

    # Perform array multiplication
    print('trig_array * local_point_array')
    print(trig_array * local_point_array)
    product_array = trig_array * local_point_array

    # Transpose array product so that addition works correctly cols must become
    # rows
    print('np.transpose(product_array)')
    print(np.transpose(product_array))

    # Perform array addition
    print('global_point_array = center_point_array + np.transpose(product_array)')
    global_point_array = center_point_array + np.transpose(product_array)
    print(global_point_array)

    # Delete extra row hanging on from addition
    print('1d global_point_array')
    global_point_array = np.delete(global_point_array, 1, axis=0)
    print(global_point_array)

    pass

def prob6_sol2(xc, yc, xp, yp, rz):
    # Default Python arithmetic solution
    c11 = np.cos(rz)
    print('C11', c11)
    c12 = -np.sin(rz)
    print('c12', c12)
    c21 = np.sin(rz)
    print('c21', c21)
    c22 = np.cos(rz)
    print('c22', c22)
    xpp = xp * c11 + yp * c12  # —-xpp,ypp=rotated coordinates relative to xc,yc
    print('xpp', xpp)
    ypp = xp * c21 + yp * c22
    print('ypp', ypp)
    xg = xc + xpp  # —-xg,yg=rotated coordinates relative to xg,yg
    yg = yc + ypp
    print('xg', xg)
    print('yg', yg)

    pass