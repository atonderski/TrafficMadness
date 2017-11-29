import pygame
from traffic_madness.drawer.pygame_drawer import PyGameDrawer
from traffic_madness.track.single_lane_track import SingleLaneTrack
from traffic_madness.config import Config


def run_simulation():
    config = Config()
    track = SingleLaneTrack(speed_limit=config.speed_limit, track_length=config.track_length,
                            max_num_cars=config.max_num_cars)
    # Add to drawer, make max_num_cars known to drawer so we can have a fixed
    # number of rects and use selective blit instead of the whole screen.
    drawer = PyGameDrawer((1000, 1000), "Traffic Madness Simulation", track)
    while True:
        track.update()
        drawer.update(track.get_car_positions())


if __name__ == '__main__':
    run_simulation()
