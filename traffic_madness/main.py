#!/usr/bin/env python
from drawer.pygame_drawer import PyGameDrawer
from track.single_lane_track import SingleLaneTrack


def run_simulation():
    track = SingleLaneTrack(speed_limit=10, track_length=1000,
                            max_num_cars=100)
    drawer = PyGameDrawer()
    while True:
        track.update()
        drawer.update(track.get_car_positions())


if __name__ == '__main__':
    run_simulation()
