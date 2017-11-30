from traffic_madness.car.simple_car import SimpleCar
from traffic_madness.car.aggressive_car import AggressiveCar
from traffic_madness.config import Config

class TrackBucket():

    def __init__(self):
        self.cars = []

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
