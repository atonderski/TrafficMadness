import itertools
from copy import deepcopy


class TrackBucket():
    """ Splits the track into buckets with each bucket containing the
        cars with positions in the interval of the bucket."""

    def __init__(self, track_length, bucket_length, num_lanes):
        """Create a bucket set. Track length need to be divisible by bucket
        length. """
        self.track_length = track_length
        self.bucket_length = bucket_length
        self.num_lanes = num_lanes
        n_buckets = float(track_length) / bucket_length
        self.bucket_list = []
        # Add flow ariable
        self.cars_leaving = 0
        if int(n_buckets) == n_buckets:
            for _ in range(int(n_buckets)):
                self.bucket_list.append([])
        else:
            raise ValueError(
                "Track length and bucket length not integer divisible")

    def _get_index_from_position(self, position):
        return int(position / self.bucket_length)

    def add_car(self, car):
        """ Adds the car to the appropriate bucket depending on its position"""
        bucket_index = self._get_index_from_position(car.position)
        self.bucket_list[bucket_index].append(car)

    def car_has_moved(self, car, old_position):
        """ Check whether the car's new position belong to a new bucket.
            If it does, it is moved and is removed from its old bucket."""
        old_bucket_index = self._get_index_from_position(old_position)
        new_bucket_index = self._get_index_from_position(car.position)

        if old_bucket_index == new_bucket_index:
            return
        else:
            # For one bucket calculate flow
            if old_bucket_index == 0:
                self.cars_leaving += 1
            self.bucket_list[old_bucket_index].remove(car)
            self.bucket_list[new_bucket_index].append(car)

    def get_num_cars(self):
        """ Returns the total sum of cars active in all buckets."""
        return sum([len(bucket) for bucket in self.bucket_list])

    def get_all_cars(self):
        """ Returns an unordered list of car objects for all cars
            active in all buckets."""
        return list(itertools.chain.from_iterable(self.bucket_list))

    def get_nearby_cars(self, position):
        """ Returns an unordered list of car objects for cars in
            (i) The bucket the position maps to
            (ii) The next bucket from the position
            (iii) The previous bucket from the position.

            Wrapping is taken into account, so if the positions bucket is the
            last bucket, the first bucket is returned as (iii)."""
        curr_ind = self._get_index_from_position(position)
        prev_ind = curr_ind - 1
        next_ind = curr_ind + 1

        nearby_cars = []
        for lane in range(self.num_lanes):
            cars_in_lane = []
            for bucket_ind in [prev_ind, curr_ind, next_ind]:
                cars_in_lane_bucket = self._get_cars_in_bucket(
                    bucket_index=bucket_ind, lane=lane)
                cars_in_lane += cars_in_lane_bucket
            nearby_cars.append(cars_in_lane)
        return nearby_cars

    def _get_cars_in_bucket(self, bucket_index, lane):
        true_bucket_index = bucket_index % len(self.bucket_list)
        cars = [car for car in self.bucket_list[true_bucket_index] if
                car.lane == lane]
        if bucket_index >= len(self.bucket_list):
            cars = [deepcopy(car) for car in cars]
            for car in cars:
                car.position += self.track_length
        if bucket_index < 0:
            cars = [deepcopy(car) for car in cars]
            for car in cars:
                car.position -= self.track_length
        cars.sort(key=lambda x: x.position)
        return cars

    def get_flow(self):
        # Temporary variable to set cars_leaving back to 0 after each time step
        temp = self.cars_leaving
        self.cars_leaving = 0
        return temp