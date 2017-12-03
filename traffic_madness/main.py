import pygame
import numpy as np
import time

from traffic_madness.config import Config
from traffic_madness.drawer.pygame_drawer import PyGameDrawer
from traffic_madness.track.multi_lane_track import MultiLaneTrack
from traffic_madness.observables.traffic_flow import traffic_flow


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

    # Define an array for averaging the traffic flow (now 1 min average)
    # equilibration needs to be at least the average time
    flow_array = np.zeros(int(60 / config.timestep))
    run = True
    start = time.time()
    while run:
        track.update()
        time_counter += 1
        # Get flow and updated flow array
        flow, flow_array = traffic_flow(track.get_flow_cars(), flow_array)
        # # Give flow to the drawer to draw it
        # drawer.update(track.get_all_cars(), time_counter, flow)

        if len(track.get_all_cars()) == config.max_num_cars:
            end = time.time()
            print('Spawning done, time %f s' % (end - start))
            equilibration = config.equilibration
            observation = config.observation
            time_counter = 0
            for i in range(0, int(equilibration / config.timestep)):
                track.update()
                time_counter += 1
                # Get flow and updated flow array
                flow, flow_array = traffic_flow(track.get_flow_cars(), flow_array)
                # # Give flow to the drawer to draw it
                # drawer.update(track.get_all_cars(), time_counter, flow)
            end = time.time()
            print('Equilibration done, time %f s' % (end - start))
            time_counter = 0
            file = open('data/flow_aggressiveness%.2f_cars%d.dat' %
                        (config.aggressives, config.max_num_cars), 'w')
            for j in range(0, int(observation / config.timestep)):
                track.update()
                time_counter += 1
                # Get flow and updated flow array
                flow, flow_array = traffic_flow(track.get_flow_cars(), flow_array)
                file.write('%f \t %f \n' % (time_counter * config.timestep, flow))
                # Give flow to the drawer to draw it
                drawer.update(track.get_all_cars(), time_counter, flow)
            file.close()
            end = time.time()
            print('Observation done, time %f s' % (end - start))
            run = False


if __name__ == '__main__':
    run_simulation()
