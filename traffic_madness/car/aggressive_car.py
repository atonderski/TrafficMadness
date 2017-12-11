from traffic_madness.config import Config
from traffic_madness.car.lane_switching_car import LaneSwitchingCar


class AggressiveCar(LaneSwitchingCar):
    def __init__(self, position, velocity, lane, nice):
        config = Config()
        super().__init__(position, velocity, lane, nice)
        self.acceleration *= config.aggressiveness
        self.deceleration *= config.aggressiveness
        self.safetymultiplier /= config.aggressiveness
        self.color = (255, 0, 0)
        self.delay_buffer = []

    def update(self, target_speed, nearby_cars):
        config = Config()
        target_speed *= config.aggressiveness

        super().update(target_speed, nearby_cars)


    def lane_is_safe(self, nearby_cars, lane, safety_distance):
        if not nearby_cars[lane]:
            return True

        dist_to_car_in_front, dist_to_car_in_back, car_in_front, car_in_back \
            = self._get_dist_to_front_and_back(nearby_cars, lane=lane)
        front_ok = (dist_to_car_in_front > safety_distance or
                    (car_in_front.velocity > self.velocity and
                     dist_to_car_in_front > self.min_distance))
        back_ok = (dist_to_car_in_back > self.min_distance)
        return front_ok and back_ok

