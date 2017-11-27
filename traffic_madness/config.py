'''global configuration file for quickly accessing and tuning parameters of the simulation'''
class Config():
    def __init__(self):
        # track properties
        self.speed_limit = 30
        self.track_length = 10000
        self.max_num_cars = 100
        self.buffer_length = 3
        # car properties
        #safety_distance = self.velocity / 2
        self.acceleration = 10
        self.deceleration = 20
        
