from copy import deepcopy

from traffic_madness.car.simple_car import SimpleCar
from traffic_madness.track import Track


class SingleLaneTrack(Track):
    def __init__(self, speed_limit, track_length, num_lanes, max_num_cars):
        self.speed_limit = speed_limit
        self.track_length = track_length
        self.num_lanes = num_lanes
        self.max_num_cars = max_num_cars
        self.cars = TrackBucket(track_length=track_length, bucket_length=25,
                                num_lanes=num_lanes)

        self.reset()

    def reset(self):
        """Puts the track in its initial state"""
        self.cars = TrackBucket(track_length, 25)
        new_car = SimpleCar(position=0,
                            velocity=self.speed_limit,
                            acceleration=1,
                            lane=0)
        self.cars.add_car(new_car)

    def update(self):
        """Performs a time step update of the entire track"""

        for car in self.cars.get_all_cars():
            old_position = car.position
            nearby_cars = self.cars.get_nearby_cars(position=car.position)
            car.update(self.speed_limit, nearby_cars)
            # Check if we need to wrap the car (periodic boundary)
            if car.position > self.track_length:
                car.position -= self.track_length
            # Inform the car tracker that the car has moved
            self.cars.car_has_moved(car=car, old_position=old_position)

        if len(self.get_num_cars()) < self.max_num_cars:
            self.try_to_spawn_car()

    def try_to_spawn_car(self):
        # Check if there is room to spawn a new car
        back_cars = self.cars.get_nearby_cars(position=0)
        for lane, cars in enumerate(back_cars):
            if any([abs(car.position - self.track_length) < buffer_length]):
                continue
            new_car = SimpleCar(position=0,
                                velocity=back_car.velocity,
                                acceleration=1,
                                lane=lane)
            self.cars.add_car(new_car)

    def get_all_cars(self):
        """Returns a list of all the car positions"""
        return self.cars.get_all_cars()
