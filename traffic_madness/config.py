'''global configuration file for quickly accessing and tuning parameters
of the simulation'''
class Config():
    def __init__(self):
        self.timestep = 0.1
        # track properties
        self.aggressives = 0.1 # % of aggressive drivers
        self.passives = 0.25 # passive drivers
        self.lanes = 5
        self.speed_limit = 20
        self.track_length = 1000
        self.buckets = float(66)
        self.max_num_cars = 150
        self.buffer_length = 500
        self.bucket_length = self.track_length / self.buckets
        # car properties
        self.acceleration = 4.3
        self.deceleration = 7.5
        self.aggressiveness = 1.2
        self.passiveness = 0.5
        self.safetymultiplier = 1.0
        self.car_length = 5.0
        
