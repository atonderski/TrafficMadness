import pygame
import numpy as np

from traffic_madness.config import Config
from traffic_madness.drawer.pygame_drawer import PyGameDrawer
from traffic_madness.track.multi_lane_track import MultiLaneTrack
from traffic_madness.observables.traffic_flow import traffic_flow


def run_simulation():
    config = Config()
    time = 0
    track = MultiLaneTrack(speed_limit=config.speed_limit,
                           track_length=config.track_length,
                           num_lanes=config.lanes,
                           max_num_cars=config.max_num_cars)
    # Add to drawer, make max_num_cars known to drawer so we can have a fixed
    # number of rects and use selective blit instead of the whole screen.
    drawer = PyGameDrawer((1000, 1000), "Traffic Madness Simulation", track)

    # Define an array for averaging the traffic flow
    flow_array = np.zeros(20)
    while True:
        track.update()
        time += 1
        # Get flow and updated flow array
        flow, flow_array = traffic_flow(track.get_flow_cars(), flow_array)
        # Give flow to the drawer to draw it
        drawer.update(track.get_all_cars(), time, flow)


if __name__ == '__main__':
    run_simulation()
