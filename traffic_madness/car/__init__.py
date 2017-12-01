from traffic_madness.config import Config

class Car:
    def __init__(self, position, velocity, lane=0):
        config = Config()
        self.position = position
        self.lane = lane
        self.velocity = velocity
        self.acceleration = config.acceleration
        self.deceleration = config.deceleration

    def update(self, target_speed, nearby_cars):
        pass
