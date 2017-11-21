from traffic_madness.car import Car
# import __init__

class SimpleCar(Car):
    def update(self, target_speed, nearby_cars):
        timestep = 1
        distances = [] # Stores distances of neighbours
        # Cannot set to 0, else cars never brake
        safety_distance = self.velocity / 2
        # Find the one in front of us
        for i in range(0, len(nearby_cars)):
            distance = nearby_cars[i].position - self.position
            distances.append(distance)
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

