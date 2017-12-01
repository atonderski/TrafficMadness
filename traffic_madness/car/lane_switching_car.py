from traffic_madness.car import Car


class LaneSwitchingCar(Car):
    def update(self, target_speed, nearby_cars):


        distances = []  # Stores distances of neighbours
        # Cannot set to 0, else cars never brake
        safety_distance = self.velocity * self.safetymultiplier

        # If car in front is too close and slower than target speed, switch
        # lane (prefer left if unoccupied)
        dist_to_car_in_front = float('inf')
        car_in_front_position = float('inf')
        for car in nearby_cars[self.lane]:
            dist = car.position - self.position
            if dist > 0:
                dist_to_car_in_front = dist
                car_in_front_position = car.position
                break

        # Speed up to speed limit if no car in front
        if dist_to_car_in_front > safety_distance:
            if self.velocity < target_speed:
                self.velocity = \
                    min([self.velocity + self.acceleration * self.timestep,
                         target_speed])
        # Slow down or shift lane if close to next car
        else:
            allowed_lanes = []
            if self.lane < len(nearby_cars) - 1:
                allowed_lanes.append(self.lane + 1)
            if self.lane > 0:
                allowed_lanes.append(self.lane - 1)
            switched_lanes = False
            for lane in allowed_lanes:
                if self.lane_is_safe(nearby_cars[lane], safety_distance):
                    self.lane = lane
                    switched_lanes = True
                    break
            if not switched_lanes:
                self.velocity = max(0, self.velocity - self.deceleration * self.timestep)
        self.update_position(car_in_front_position)

        assert self.velocity >= 0
    
    def update_position(self, car_in_front_position):
        """ Updates the position of the car. If it reaches the 
            position of the car in front, the cars collide.
            Passing not allowed except for lane switching."""
        proposed_position = self.position + self.velocity * self.timestep
        # TODO(CHANGE THIS DANIEL): This should not be - own length, send car instead
        crash_position = car_in_front_position - self.length
        if proposed_position > crash_position and self.position > crash_position:
            # We stay at the same spot until car in front moves
            self.velocity = 0
        elif proposed_position > car_in_front_position and self.position < crash_position:
           self.position = crash_position
           self.velocity = 0
        else:
            self.position = proposed_position

    def lane_is_safe(self, cars_in_lane, safety_distance):
        if not cars_in_lane:
            return True
        distances = [abs(car.position - self.position) for car in cars_in_lane]
        return min(distances) > safety_distance
