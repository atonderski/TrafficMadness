'''global configuration file for quickly accessing and tuning parameters
of the simulation'''
class Config():
    def __init__(self):
        # track properties
        self.speed_limit = 30
        self.track_length = 1000
        self.max_num_cars = 100
        self.buffer_length = 3
        # car properties
        self.acceleration = 4.3
        self.deceleration = 7.5
        self.aggressiveness = 1.1
        
