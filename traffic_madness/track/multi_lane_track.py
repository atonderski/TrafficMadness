import numpy as np

from traffic_madness.car.aggressive_car import AggressiveCar
from traffic_madness.car.lane_switching_car import LaneSwitchingCar
from traffic_madness.car.passive_car import PassiveCar
from traffic_madness.config import Config
from traffic_madness.track import Track
from traffic_madness.track.trackbucket import TrackBucket


class MultiLaneTrack(Track):
    def __init__(self, speed_limit, track_length, num_lanes, max_num_cars):
        self.speed_limit = speed_limit
        self.track_length = track_length
        self.num_lanes = num_lanes
        self.max_num_cars = max_num_cars
        self.cars = None
        self.cartypes = [0, 0, 0]  # Counter for different car types
        # [Aggressive, neutral, passive]
        self.config = Config()
        self.spawn_nice_cars = self.config.nice_cars
        self.buffer_length = self.config.buffer_length

        self.reset()

    def spawn_all_cars(self):
        for i in range(self.max_num_cars):
            position = self.track_length*i/(self.max_num_cars);
            position += 2*(np.random.random()-0.5)
            lane = i%3;
            random_nbr = np.random.random()

            # Spawn cars at random position, fills track faster and does not
            # produce a biased
            # congestion.
            if random_nbr < self.config.aggressives:
                new_car = AggressiveCar(
                    position=position,
                    velocity=self.speed_limit,
                    lane=lane,
                    nice=self.spawn_nice_cars)
                self.cartypes[0] += 1
            elif random_nbr < self.config.aggressives + self.config.passives:
                new_car = PassiveCar(
                    position=position,
                    velocity=self.speed_limit,
                    lane=lane,
                    nice=self.spawn_nice_cars)
                self.cartypes[2] += 1
            else:
                new_car = LaneSwitchingCar(
                    position=position,
                    velocity=self.speed_limit,
                    lane=lane,
                    nice=self.spawn_nice_cars)
                self.cartypes[1] += 1
            self.cars.add_car(new_car)


    def reset(self):
        config = Config()
        """Puts the track in its initial state"""
        self.cars = TrackBucket(track_length=self.track_length,
                                bucket_length=config.bucket_length,
                                num_lanes=self.num_lanes)
        self.spawn_all_cars()

    def update(self):
        """Performs a time step update of the entire track.
           The current time is the loop iteration times the time
           step used in the model. The actual time the cars see."""

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

        # Spawn cars at random position, fills track faster and does not
        # produce a biased
        # congestion.
        if random_nbr < config.aggressives:
            new_car = AggressiveCar(
                position=np.random.uniform(0.0, config.track_length),
                velocity=self.speed_limit,
                lane=np.random.randint(0, 2),
                nice=self.spawn_nice_cars)
            self.cartypes[0] += 1
        elif random_nbr < config.aggressives + config.passives:
            new_car = PassiveCar(
                position=np.random.uniform(0.0, config.track_length),
                velocity=self.speed_limit,
                lane=np.random.randint(0, 2),
                nice=self.spawn_nice_cars)
            self.cartypes[2] += 1
        else:
            new_car = LaneSwitchingCar(
                position=np.random.uniform(0.0, config.track_length),
                velocity=self.speed_limit,
                lane=np.random.randint(0, 2),
                nice=self.spawn_nice_cars)
            self.cartypes[1] += 1
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

    def get_max_density_index(self, disturbed_car):
        """Returns the bucket index of the disturbed car and
           the bucket index of the car with the maximum density"""
        return self.cars.get_max_density_index(disturbed_car)


    def get_all_cars(self):
        """Returns a list of all car positions"""
        return self.cars.get_all_cars()

    def get_flow_cars(self):
        # Get number of cars that left a bucket this timestep
        return self.cars.get_flow()

    def get_cartypes(self):
        return self.cartypes
