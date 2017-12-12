import pygame
import numpy as np
import time

from traffic_madness.config import Config
from traffic_madness.drawer.pygame_drawer import PyGameDrawer
from traffic_madness.track.multi_lane_track import MultiLaneTrack
import traffic_madness.observables.traffic_flow as tf
import traffic_madness.observables.speed_averages as sa


def run_simulation():
    # Change this to False to not draw
    config = Config()
    time_counter = 0
    track = MultiLaneTrack(speed_limit=config.speed_limit,
                           track_length=config.track_length,
                           num_lanes=config.lanes,
                           max_num_cars=config.max_num_cars)
    # Add to drawer, make max_num_cars known to drawer so we can have a fixed
    # number of rects and use selective blit instead of the whole screen.
    if draw_all:
        drawer = PyGameDrawer((1000, 1000), "Traffic Madness Simulation", track)
    else:
        drawer = 0
    # Define an array for averaging the traffic flow (now 1 min average)
    # equilibration needs to be at least the average time

    spawning(track, drawer)
    equilibration(track, drawer)
    car_to_disturb = get_disturbed_car(track)
    observation(track, drawer, 'before', car_to_disturb)
    create_disturbance(car_to_disturb)
    observation(track, drawer, 'after', car_to_disturb)
    undisturb_car(car_to_disturb)
    observation(track, drawer, 'final', car_to_disturb)

def undisturb_car(disturb_car):
    disturb_car.stuck = False


def get_disturbed_car(track):
    all_cars = track.get_all_cars()
    index = np.random.randint(0, len(all_cars) - 1)
    return all_cars[index]


def create_disturbance(disturb_car):
    disturb_car.velocity = 0
    disturb_car.color = (0, 0, 0)
    disturb_car.stuck = True


# Spawning phase for all cars
def spawning(track, drawer):
    config = Config()
    time_counter = 0
    while len(track.get_all_cars()) < config.max_num_cars:
        track.update()
        time_counter += 1
        #  Give flow to the drawer to draw it
        if draw_all:
            drawer.update(track.get_all_cars(), time_counter, 0)


def equilibration(track, drawer):
    config = Config()
    optimal_flow = tf.optimal_flow(track.get_cartypes())
    time_counter = 0
    while time_counter * config.timestep < config.equilibration:
        track.update()
        time_counter += 1
        # Get flow and updated flow array
        flow = tf.traffic_flow(track.get_flow_cars())
        flow /= optimal_flow
        # # Give flow to the drawer to draw it
        if draw_all:
            drawer.update(track.get_all_cars(), time_counter, flow)
    print('Done equilibration')

def observation(track, drawer, eq, disturbed_car):
    config = Config()
    time_counter = 0
    cartypes = track.get_cartypes()
    optimal_flow = tf.optimal_flow(cartypes)
    optimal_speed = sa.get_optimal_speed(cartypes)
    file = open('data/tmp/aggressives{:.2f}{}.dat'.format(cartypes[0] / 
        config.max_num_cars, eq), 'w')
    file.write('# Optimal flow and avg speed dependent on time \n '
               '# Aggressives: {} \n'.format(cartypes[0]))
    while time_counter * config.timestep < config.observation:
        track.update()
        time_counter += 1
        # Get flow and updated flow array
        speed = sa.global_average_speed(track.get_all_cars())/optimal_speed
        flow = tf.traffic_flow(track.get_flow_cars())
        flow /= optimal_flow
        bucket_disturbed, bucket_max_density = track.get_max_density_index(disturbed_car)
        # Data in file Tab: time flow avg vel index of disturbance, index of
        # max density
        file.write('{:.2f} \t {:.4f} \t {:.4f} \t {} \t {} \n'.format(time_counter * config.timestep, flow, speed, bucket_disturbed, bucket_max_density))
        # # Give flow to the drawer to draw it
        if draw_all:
            drawer.update(track.get_all_cars(), time_counter, flow)
    file.close()
    print('Done observation ' + eq)


if __name__ == '__main__':
    draw_all = False
    start = time.time()
    run_simulation()
    print('Done in {:.0f}'.format(time.time()-start))
