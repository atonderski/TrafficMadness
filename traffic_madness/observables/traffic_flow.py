import numpy as np
from traffic_madness.config import Config

# Function gets the cars leaving a bucket as input and averages over
# a certain number of timesteps (length of flows)
def traffic_flow(cars_moved, flows):
    config = Config()
    flows = np.delete(flows, 0)
    flows = np.append(flows, cars_moved)
    average = np.average(flows)
    # Get flow in cars per hour (Unit of timestep is seconds)
    multiplicator = 1 / config.timestep * 3600
    return average * multiplicator, flows