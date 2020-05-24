import numpy as np
import pickle
from helpers import est_integral, est_derivative, show_pos_scatter

"""
Functions to create samples of vehicle motion data
"""
# creates a sample of motion data based on parabola-shaped velocities
def simple_motion(dt,tmax):
    times = np.linspace(0, tmax, num = np.floor((tmax+dt)/dt))
    
    # defining parabola-shaped velocity
    vel = np.zeros([2,len(times)])

    # x-direction: one random parabola
    vel[0,:] = 30*np.sin(times * 2 * np.pi / tmax)
    #vel[0,:] = -0.025*times**2 + 5*times

    # y-directin: another random parabola
    vel[1,:] = -0.015*times**2 + 25

    # get position as integral of velocity
    pos = est_integral(vel,times)

    # get accerlation as derivative of velocity
    acc = est_derivative(vel,times)

    return times, pos, vel, acc

"""
Saving vehicle data to a file
"""
def save_data(t,p,v,a,filename):
    trajectory = [t, p, v, a]
    with open(filename, 'wb') as f:
        pickle.dump(trajectory, f)

###############################################################################

"""
Generating some sample car truth data
"""

tmax = 60   # maximum time is seconds
dt = 0.1      # time between data points

t,p,v,a = simple_motion(dt,tmax)
show_pos_scatter(p)
save_data(t,p,v,a,'sample_trajectory.pickle')
