'''global configuration file for quickly accessing and tuning parameters
of the simulation'''
class Config():
    def __init__(self):
        self.timestep = 0.1
        # track properties
        self.lanes = 5
        self.speed_limit = 20
        self.track_length = 1000
        self.max_num_cars = 150
        self.buffer_length = 20
        self.bucket_length = 50
        # car properties
        self.acceleration = 4.3
        self.deceleration = 7.5
        self.aggressiveness = 1.2
        self.safetymultiplier = 1.0
        
