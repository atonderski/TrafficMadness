import pygame
from traffic_madness.drawer.pygame_drawer import PyGameDrawer
from traffic_madness.track.single_lane_track import SingleLaneTrack


def run_simulation():
    track = SingleLaneTrack(speed_limit=8, track_length=1000,
                            max_num_cars=500)
    # Add to drawer, make max_num_cars known to drawer so we can have a fixed number of rects and use selective blit instead of the whole screen.
    drawer = PyGameDrawer((1000, 1000), "Traffic Madness Simulation", track)
    while True:
        track.update()
        drawer.update(track.get_car_positions())


if __name__ == '__main__':
    run_simulation()
