import matplotlib.pyplot as plt
import numpy as np


def prob6_sol1(xc, yc, xp, yp, rz):
    #convert to radians
    rz = rz * np.pi/180
    print('rz in radians')
    print(rz)

    # Numpy solution with comments
    # Set up array with trig functions with rotation angle arg
    trig_array = np.array([[np.cos(rz), -np.sin(rz)], [np.sin(rz), np.cos(rz)]])
    print('trig_array')
    print(trig_array)


    # Set up array with local points
    local_point_array = np.array([xp, yp])
    print('local_point_array')
    print(local_point_array)

    # Set up array with center coords
    center_point_array = np.array([xc, yc])
    print('center_point_array')
    print(center_point_array)

    # Perform array multiplication (not element by element)
    print(np.matmul(trig_array, local_point_array))
    print('matmul(trig_array, local_point_array)')
    product_array = np.matmul(trig_array, local_point_array)

    # Perform array addition
    global_point_array = center_point_array + product_array
    print('global_point_array = center_point_array + product_array')
    print("- - new global points - - ")
    print(global_point_array)

    pass

def prob6_sol2(xc, yc, xp, yp, rz):
    # convert to radians
    rz = rz * np.pi / 180

    print(rz)

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
    print("- - new global points - - ")
    print('xg', xg, 'yg', yg)

    pass