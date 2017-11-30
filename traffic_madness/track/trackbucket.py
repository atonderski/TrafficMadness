from traffic_madness.car.simple_car import SimpleCar
from traffic_madness.car.aggressive_car import AggressiveCar
from traffic_madness.config import Config

class TrackBucket():

    def __init__(self, track_length, bucket_length, num_lanes):
        self.track_length = track_length
        self.bucket_length = bucket_length
        self.num_lanes = num_lanes
        n_buckets = track_length/bucket_length
        self.bucket_list = []
        if n_buckets % 1 == 0:
            for i in range(int(n_buckets)):
                self.bucket_list.append([])
        else:
            raise ValueError("Track length and bucket length not integer divisible")

    def add_car(self, car):
        """ Adds the car to the appropriate bucket depending on its position"""
        bucket_index = int(car.position/self.bucket_length)
        self.bucket_list[bucket_index].append(car)

    def car_has_moved(self, car, old_position):
        """ Check whether the car's new position belong to a new bucket."""
        old_bucket = int(old_position/self.bucket_length)
        new_bucket = int(car.position/self.bucket_length)

    def get_num_cars():
        [
    def get_all_cars():
        

    def get_nearby(self, position):

    def get_position_list(self):
        """Computes a numpy vector of positions with the indices matching the indices in
            the lanes car list.
            
            Returns: empty vector if car list is empty
                     position_list row vector if not"""
        if self.cars:
            position_list = np.asarray([car.position for car in self.cars])
        elif not self.cars:
            position_list = np.empty()

        return position_list

    def add_cars(self, new_cars):
        """Takes a list of cars [car1, car2, car3] and extends the car list
        by adding the new cars to the end. Only use this for spawning"""
        self.cars.append(cars)

    def insert_cars(self, new_cars):
        """Takes a list of cars [car1, car2, car3] and inserts them at the
            appropriate index depending on their position."""
        new_positions = [] 
