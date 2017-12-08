'''global configuration file for quickly accessing and tuning parameters
of the simulation'''
class Config():
    def __init__(self):
        self.timestep = 0.05
        self.equilibration = 120 # Set equilibration time
        self.observation = 180 # Set time for observation
        self.fps = 60
        # track properties
        self.aggressives = 0.2 # % of aggressive drivers
        self.passives = 0.0 # passive drivers
        self.lanes = 3
        self.speed_limit = 20
        self.track_length = 1000
        self.buckets = 40.0
        self.max_num_cars = 200
        self.buffer_length = 10
        self.bucket_length = self.track_length / self.buckets
        # car properties
        self.acceleration = 2.3
        self.deceleration = 0.5
        self.aggressiveness = 1.2
        self.passiveness = 0.8
        self.safetymultiplier = 0.7
        self.car_length = 5.0
#        self.delay_buffer_length = 2
        self.reaction_time = 1.0 # Seconds between deacceleration
