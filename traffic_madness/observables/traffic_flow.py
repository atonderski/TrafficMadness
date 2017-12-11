import numpy as np
from traffic_madness.config import Config

# Function gets the cars leaving a bucket as input and averages over
# a certain number of timesteps (length of flows)
def traffic_flow(cars_moved):
    config = Config()
    # flows = np.delete(flows, 0)
    # flows = np.append(flows, cars_moved)
    # average = np.average(flows)
    # Get flow in cars per hour (Unit of timestep is seconds)
    multiplicator = 1 / config.timestep * 3600
    # return average * multiplicator, flows
    return cars_moved * multiplicator

def optimal_flow(cartypes):
    config = Config()
    aggressives = cartypes[0]
    neutrals = cartypes[1]
    passives = cartypes[2]
    # Flow of neutral cars
    flow = (config.speed_limit / config.track_length) * neutrals
    # Flow of aggressive cars
    flow += (config.speed_limit * config.aggressiveness/ config.track_length)\
            * aggressives
    # Flow of passive cars
    flow += (config.speed_limit * config.passiveness / config.track_length) \
            * passives
    # Rescale to cars per hour
    flow *= 3600
    return flow
