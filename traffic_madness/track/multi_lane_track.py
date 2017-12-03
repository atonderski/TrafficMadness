from copy import deepcopy

from traffic_madness.car.lane_switching_car import LaneSwitchingCar
from traffic_madness.car.aggressive_car import AggressiveCar
from traffic_madness.car.passive_car import PassiveCar
from traffic_madness.car.simple_car import SimpleCar
from traffic_madness.track import Track
from traffic_madness.track.trackbucket import TrackBucket
from traffic_madness.config import Config
import numpy as np

class MultiLaneTrack(Track):
    def __init__(self, speed_limit, track_length, num_lanes, max_num_cars):
        self.speed_limit = speed_limit
        self.track_length = track_length
        self.num_lanes = num_lanes
        self.max_num_cars = max_num_cars
        self.cars = None
        config = Config()

        self.buffer_length = config.buffer_length

        self.reset()

    def reset(self):
        config = Config()
        """Puts the track in its initial state"""
        self.cars = TrackBucket(track_length=self.track_length,
                                bucket_length=config.bucket_length,
                                num_lanes=self.num_lanes)

    def update(self):
        """Performs a time step update of the entire track"""

        for car in self.cars.get_all_cars():
            old_position = car.position
            nearby_cars = self.cars.get_nearby_cars(position=car.position)
            nearby_cars[car.lane].remove(car)
            car.update(self.speed_limit, nearby_cars)
            # Check if we need to wrap the car (periodic boundary)
            if car.position >= self.track_length:
                car.position -= self.track_length
            elif car.position < 0:
                car.position += self.track_length
            # Inform the car tracker that the car has moved
            self.cars.car_has_moved(car=car, old_position=old_position)

        if self.cars.get_num_cars() < self.max_num_cars:
            # self.try_to_spawn_car()
            self.try_to_spawn_car_single_lane(lane=0)

    def try_to_spawn_car_single_lane(self, lane):
        config = Config()
        # Check if there is room to spawn a new car
        back_cars = self.cars.get_nearby_cars(position=0)
        cars = back_cars[lane]
        if any([abs(car.position) < self.buffer_length for
                car in cars]):
            return

        random_nbr = np.random.random()
        # if random_nbr < config.aggressives:
        #     new_car = AggressiveCar(position=0,
        #                            velocity=self.speed_limit,
        #                            lane=lane)
        # elif random_nbr < config.aggressives + config.passives:
        #     new_car = PassiveCar(position=0,
        #                            velocity=self.speed_limit,
        #                            lane=lane)
        # else:
        #     new_car = LaneSwitchingCar(position=0,
        #                                velocity=self.speed_limit,
        #                                lane=lane)

        # Spawn cars at random position, fills track faster and does not produce a biased
        # congestion. 
        if random_nbr < config.aggressives:
            new_car = AggressiveCar(position=np.random.uniform(0.0, config.track_length),
                                   velocity=self.speed_limit,
                                   lane=lane)
        elif random_nbr < config.aggressives + config.passives:
            new_car = PassiveCar(position=np.random.uniform(0.0, config.track_length),
                                   velocity=self.speed_limit,
                                   lane=lane)
        else:
            new_car = LaneSwitchingCar(position=np.random.uniform(0.0, config.track_length),
                                       velocity=self.speed_limit,
                                       lane=lane)
        self.cars.add_car(new_car)

    def try_to_spawn_car(self):
        # Check if there is room to spawn a new car
        back_cars = self.cars.get_nearby_cars(position=0)
        for lane, cars in enumerate(back_cars):
            if any([abs(car.position - 0) < self.buffer_length
                    for car in cars]):
                continue
            new_car = LaneSwitchingCar(position=0,
                                       velocity=self.speed_limit,
                                       lane=lane)
            self.cars.add_car(new_car)

    def get_all_cars(self):
        """Returns a list of all the car positions"""
        return self.cars.get_all_cars()

    def get_flow_cars(self):
        # Get number of cars that left a bucket this timestep
        return self.cars.get_flow()
