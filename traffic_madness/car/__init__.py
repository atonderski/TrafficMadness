class Car:
    def __init__(self, position, lane, velocity, acceleration):
        self.position = position
        self.lane = lane
        self.velocity = velocity
        self.acceleration = 4.3 # Add capability of acceleration
        self.deceleration = 7.5

    def update(self, target_speed, nearby_cars):
        pass
