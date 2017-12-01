'''global configuration file for quickly accessing and tuning parameters
of the simulation'''
class Config():
    def __init__(self):
        self.timestep = 0.1
        # track properties
        self.speed_limit = 5
        self.track_length = 100
        self.max_num_cars = 150
        self.buffer_length = 3
        self.bucket_length = 25
        # car properties
        self.acceleration = 1.3
        self.deceleration = 50.0
        self.aggressiveness = 1.1
        self.safetymultiplier = 1.0
        
