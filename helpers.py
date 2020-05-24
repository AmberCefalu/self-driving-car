import numpy as np
import pickle
from matplotlib import pyplot as plt


"""
Manipulating data, mathematical operations, etc.
"""
# estimating the integral of a time series data
def est_integral(data,times):
    dim = np.size(data,0)
    integral = np.zeros([dim,len(times)])

    # calculate integral for each dimension of data
    for i in range(dim):
        # assume a starting value of zero
        integral[i,0] = 0.0 
        area = 0.0 

        last_t = times[0]
        for j in range(1,len(times)):
            dt = times[j] - last_t
            area += dt * data[i,j]
            integral[i,j] = area
            last_t = times[j]

    return integral

# estimating the derivative of a time series data
def est_derivative(data,times):
    dim = np.size(data,0)
    derivative = np.zeros([dim,len(times)])

    # calculate the derivative for each dimension of data
    for i in range(dim):
        # assume a starting value of zero
        derivative[i,0] = 0.0

        last_y = data[i,0]
        last_t = times[0]
        for j in range(1,len(times)):
            dy = data[i,j] - last_y
            dt = times[j] - last_t
            derivative[i,j] = dy / dt
            last_y = data[i,j]
            last_t = times[j]

    return derivative

"""
Plotting functions
"""
def show_pos_scatter(pos):
    if np.size(pos,0) != 2:
        # plot only works for 2D position data
        ValueError('Position vector must be 2 x N')
    
    x = pos[0,:]
    y = pos[1,:]

    plt.scatter(x,y)
    plt.plot(x,y)
    plt.title('Vehicle Position')
    plt.xlabel('x position (m)')
    plt.ylabel('y position (m)')
    plt.show()

"""
Read input data files
"""
def input_data(filename):
    with open(filename, 'rb') as f:
        data = pickle.load(f)
    return list(data)
