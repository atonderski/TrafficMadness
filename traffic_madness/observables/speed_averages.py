import numpy as np
from itertools import groupby
from traffic_madness.config import Config

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
    print(class_velocities, class_names)

