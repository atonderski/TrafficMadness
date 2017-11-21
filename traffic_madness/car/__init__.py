
class Car:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def update(self, target_speed, nearby_cars):
        timestep = 1
        self.position += self.velocty * timestep
        pass