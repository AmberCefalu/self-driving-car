from helpers import input_data

"""
Runs the main program
"""

# get sample trajectory data
filename = 'sample_trajectory.pickle'
data = input_data(filename)

# unpack the data
times = data[0]
pos = data[1]
vel = data[2]
acc = data[3]
