from traffic_madness.drawer.pygame_drawer import PyGameDrawer
from traffic_madness.track.single_lane_track import SingleLaneTrack


def run_simulation():
    track = SingleLaneTrack()
    drawer = PyGameDrawer()
    while True:
        track.update()
        drawer.update(track.get_car_positions())


if __name__ == '__main__':
    run_simulation()