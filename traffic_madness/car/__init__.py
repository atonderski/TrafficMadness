from traffic_madness.config import Config


class Car:
    def __init__(self, position, velocity, lane=0, nice=False):
        config = Config()
        self.nice = nice
        self.delay_buffer_length = config.delay_buffer_length
        self.timestep = config.timestep
        self.safetymultiplier = config.safetymultiplier
        self.position = position
        self.lane = lane
        self.velocity = velocity
        self.acceleration = config.acceleration
        self.deceleration = config.deceleration
        self.length = config.car_length
        self.color = (0, 0, 255)
        # self.color = (64 + random.randint(0, 127),
        #               64 + random.randint(0, 127),
        #               64 + random.randint(0, 127))
        self.delay_buffer = []

    def update(self, target_speed, nearby_cars):
        pass
