import pygame
import numpy as np
import time

from traffic_madness.config import Config
from traffic_madness.drawer.pygame_drawer import PyGameDrawer
from traffic_madness.track.multi_lane_track import MultiLaneTrack
import traffic_madness.observables.traffic_flow as tf


def run_simulation():
    config = Config()
    time_counter = 0
    track = MultiLaneTrack(speed_limit=config.speed_limit,
                           track_length=config.track_length,
                           num_lanes=config.lanes,
                           max_num_cars=config.max_num_cars)
    # Add to drawer, make max_num_cars known to drawer so we can have a fixed
    # number of rects and use selective blit instead of the whole screen.
    drawer = PyGameDrawer((1000, 1000), "Traffic Madness Simulation", track)
    #drawer = 0
    # Define an array for averaging the traffic flow (now 1 min average)
    # equilibration needs to be at least the average time
    flow_array = np.zeros(int(60 / config.timestep))

    spawning(track, drawer)
    flow_array = equilibration(track, drawer, flow_array)
    observation(track, drawer, flow_array)


# Spawning phase for all cars
def spawning(track, drawer):
    config = Config()
    time_counter = 0
    while len(track.get_all_cars()) < config.max_num_cars:
        track.update()
        time_counter += 1
        #  Give flow to the drawer to draw it
        drawer.update(track.get_all_cars(), time_counter, 0)


def equilibration(track, drawer, flow_array):
    config = Config()
    optimal_flow = tf.optimal_flow(track.get_cartypes())
    time_counter = 0
    print(optimal_flow)
    while time_counter * config.timestep < config.equilibration:
        track.update()
        time_counter += 1
        # Get flow and updated flow array
        flow, flow_array = tf.traffic_flow(track.get_flow_cars(), flow_array)
        flow /= optimal_flow
        # # Give flow to the drawer to draw it
        drawer.update(track.get_all_cars(), time_counter, flow)
    return flow_array

def observation(track, drawer, flow_array):
    config = Config()
    time_counter = 0
    cartypes = track.get_cartypes()
    optimal_flow = tf.optimal_flow(cartypes)
    file = open('data/flow_aggressives_100cars/aggressives{:.2f}.dat'.format(cartypes[0] / config.max_num_cars),
                'w')
    file.write('# Optimal flow dependent on time \n '
               '# Aggressives: {} \n'.format(cartypes[0]))
    while time_counter * config.timestep < config.observation:
        track.update()
        time_counter += 1
        # Get flow and updated flow array
        flow, flow_array = tf.traffic_flow(track.get_flow_cars(), flow_array)
        flow /= optimal_flow
        file.write('{:.2f} \t {:.4f} \n'.format(time_counter * config.timestep, flow))
        # # Give flow to the drawer to draw it
        drawer.update(track.get_all_cars(), time_counter, flow)
    file.close()


if __name__ == '__main__':
    run_simulation()
