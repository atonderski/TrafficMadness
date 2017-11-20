'''
A simple sketch of terminal style rendering of a few cars, and how the car objects could be
represented as arrays (or matrices). You might want to scale road_length to the width of your
terminal or you will be seeing some strange rendering behaviour. 
TODO: 
- car positions and velocities are currently represented as simple arrays. This should be done in numpy, or the car properties should be abstracted away as a class. 
- The rendering should be abstracted away as a function of the underlying datastructures (i.e. Car, or a numpy matrix.
- more advanced time stepping behaviour (i.e. collision, slowdown when there are cars in close proximity. 
- time optimizations: currently running ~O(n^2), this could probably be optimized down to ~O(n) with linked lists and the like 
- A relic where a single car is running on the track takes up roughly half the code and is completely redundant.
- Feel free to improve (or discard) upon this however you like :), this is just to get the first few lines of code down in order to get the ball rolling. 
'''

import sys
import time
import numpy
road_length = 100

car_position = 3;
car_speed = 10;

number_of_cars = 1;

#init, position and velocities for car i
car_positions=[3,5]; 
car_velocities=[1,1]; # these two vectors have to be the same length

sleep_time=3;

print("starting main loop...");
running = True
single_render = False;
while running: # main loop
    if (single_render): # render a single car
        for x in range(1,road_length):
        
            if (round(car_position) == x): # rendered parts of track are integer values
                sys.stdout.write('x')
                sys.stdout.flush();
            else:
                sys.stdout.write('-')
                sys.stdout.flush();

        # slow down
        time.sleep(sleep_time)
        # carriage return
        sys.stdout.write('\r')
        sys.stdout.flush();
    else: # render the arrays of cars
        time.sleep(sleep_time);
        #carriage return
        sys.stdout.write('\r')
        sys.stdout.flush()
        for i in range(1,road_length):
            for j in range(0,len(car_positions)):
                if (round(car_positions[j]) == i): # there's a car at rendered position
                    sys.stdout.write('x')
                    sys.stdout.flush()
                    continue # there could be multiple cars in the same spot
                else:
                    sys.stdout.write('-')
                    sys.stdout.flush()
        
    # update array positions
    for i in range(0,len(car_positions)):
        car_positions[i] = car_positions[i] + car_velocities[i]
        if (car_positions[i] > road_length):
            car_positions[i] = car_positions[i] - road_length
        

    #update car position
    car_position = car_position + car_speed;

    #periodic boundary conditions, cars only drive one way
    if (car_position > road_length):
        car_position = car_position - road_length

    
    
    
