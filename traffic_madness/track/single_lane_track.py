from traffic_madness.track import Track


class SingleLaneTrack(Track):
    def __init__(self, speed_limit):
        self.speed_limit = speed_limit
        self.cars = []

    def update(self):
        # Update positions of all current cars
        for i, car in enumerate(self.cars):
            if len(self.cars) > 1:
                next_index = (i + 1) % len(self.cars)
                nearby_cars = [self.cars[i - 1], self.cars[next_index]]
            else:
                nearby_cars = []
            car.update(self.speed_limit, nearby_cars)

        # Check if we should spawn new cars

        return

    def get_car_positions(self):
        return [car.position for car in self.cars]