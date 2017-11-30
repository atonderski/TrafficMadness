from traffic_madness.car.simple_car import SimpleCar
from traffic_madness.car.aggressive_car import AggressiveCar
from traffic_madness.config import Config

class TrackBucket():
    """ Splits the track into buckets with each bucket containing the
        cars with positions in the interval of the bucket."""

    def __init__(self, track_length, bucket_length, num_lanes):
        """Create a bucket set. Track length need to be divisible by bucket length. """
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
        """ Check whether the car's new position belong to a new bucket.
            If it does, it is moved and is removed from its old bucket."""
        old_bucket_index = self._get_index_from_position(old_position)  
        new_bucket_index = self._get_index_from_position(new_position)

        if old_bucket_index == new_bucket_index:
            return
        else:
            self.bucket_list[old_bucket_index].remove(car)
            self.bucket_list[new_bucket_index].append(car)
            
    def get_num_cars():
        """ Returns the total sum of cars active in all buckets."""

    def get_all_cars():
        """ Returns an unordered list of car objects for all cars 
            active in all buckets."""

    def get_nearby(self, position):
        """ Returns an unordered list of car objects for cars in
            (i) The bucket the position maps to
            (ii) The next bucket from the position
            (iii) The previous bucket from the position.
            
            Wrapping is taken into account, so if the positions bucket is the
            last bucket, the first bucket is returned as (iii)."""

