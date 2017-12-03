import numpy as np

# Function gets the cars leaving a bucket as input and averages over
# a certain number of timesteps (length of flows)
def traffic_flow(cars_moved, flows):
    flows = np.delete(flows, 0)
    flows = np.append(flows, cars_moved)
    return np.average(flows), flows