from traffic_madness.car import Car

class SimpleCar(Car):
    def update(self, target_speed, nearby_cars):
        # TODO Remove this and add multi lane logic
        nearby_cars = nearby_cars[self.lane]

        timestep = 1
        distances = [] # Stores distances of neighbours
        # Cannot set to 0, else cars never brake
        safety_distance = self.velocity * 1.8
        # Find the one in front of us
        for i in range(0, len(nearby_cars[self.lane][:])):
            distance = nearby_cars[i].position - self.position
            distances.append(distance)


        ''' nearby_cars stored cars in a matrix where first index gives the 
        lane and the second index is 0 for the car in front and 1 for the car in the
        back '''
        for i in range(0, 3):
            temp = []
            for j in range(0, 2):
                # Create a distance array with same dimensions as nearby_cars
                temp.append(nearby_cars[i][j].position - self.position)
            distances.append(temp)
        # Decide if we want to brake or accelerate

        if not distances or max(distances) >= safety_distance:
            if self.velocity < target_speed:
                # If there is room and car is below speed limit, accelerate
                self.velocity = \
                    min([self. velocity + self.acceleration * timestep,
                                      target_speed])
            self.position += self.velocity * timestep

        elif max(distances) < safety_distance:
            self.velocity -= self.acceleration * timestep
            self.position += self.velocity * timestep
