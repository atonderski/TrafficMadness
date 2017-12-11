import numpy as np
from itertools import groupby
from traffic_madness.config import Config

def get_optimal_speed(cartypes):
    config = Config()
    aggressives = cartypes[0]
    neutrals = cartypes[1]
    passives = cartypes[2]
    # Speed of neutral cars
    speed = (config.speed_limit) * neutrals
    # Speed of aggressive cars
    speed += (config.speed_limit * config.aggressiveness)* aggressives
    # Flow of passive cars
    speed += (config.speed_limit * config.passiveness)* passives
    # Rescale to cars per hour
    speed *= 1/(aggressives+neutrals+passives)
    return speed

def global_average_speed(cars):
    """Return the instantaneous average velocity averaged over all cars"""
    velocities = [car.velocity for car in cars]
    average_speed = sum(velocities)/len(cars)
    return average_speed

def class_average_speed(cars):
    """Return the instantaneous average velocity for each class of cars
    
        Return class_velocity - list of average velocities for class in class_names
               class_names - list of class names of active cars 
    """
    # Sort by class name
    class_sorted = sorted(cars, key=lambda car: type(car).__name__)
    class_velocities = []
    class_names = []
    # Group the cars of same class and average their velocities, save class names
    for key, group in groupby(cars, key=lambda car: type(car).__name__):
        velocities = [car.velocity for car in group]
        class_velocity = sum(velocities) / len(velocities)
        class_velocities.append([class_velocity])
        class_names.append(key)
    return class_velocities, class_names
