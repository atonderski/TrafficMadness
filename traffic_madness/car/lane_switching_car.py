from traffic_madness.car import Car


class LaneSwitchingCar(Car):
    def update(self, target_speed, nearby_cars):
        # Cannot set to 0, else cars never brake
        safety_distance = self.velocity * self.safetymultiplier

        dist_to_car_in_front, dist_to_car_in_back = \
            self._get_dist_to_front_and_back(nearby_cars)

        # Switch lanes if we are too close in front or back
        switched = False
        if dist_to_car_in_front < safety_distance:
            switched = self.attempt_lane_shift(target_speed,
                                               nearby_cars,
                                               safety_distance)
        elif abs(dist_to_car_in_back) < safety_distance:
            switched = self.attempt_lane_shift(target_speed,
                                               nearby_cars,
                                               safety_distance,
                                               prefer_right=True)

        # Update distances if we switched lanes
        if switched:
            dist_to_car_in_front, dist_to_car_in_back = \
                self._get_dist_to_front_and_back(nearby_cars)

        # Speed up to speed limit if no car in front
        if dist_to_car_in_front > safety_distance:
            if self.velocity < target_speed:
                self.velocity = \
                    min([self.velocity + self.acceleration * self.timestep,
                         target_speed])
        else:
            self.velocity = max(
                0, self.velocity - self.deceleration * self.timestep)

        self.position += self.velocity * self.timestep

        assert self.velocity >= 0

    def _get_dist_to_front_and_back(self, nearby_cars):
        dist_to_car_in_front = float('inf')
        dist_to_car_in_back = -float('inf')
        for car in nearby_cars[self.lane]:
            dist = car.position - self.position
            if dist > 0 and dist < dist_to_car_in_front:
                dist_to_car_in_front = dist
            elif dist < 0 and dist > dist_to_car_in_back:
                dist_to_car_in_back = dist
        return dist_to_car_in_front, dist_to_car_in_back

    def attempt_lane_shift(self, target_speed, nearby_cars, safety_distance,
                           prefer_right=True):

        # Check lane shift
        allowed_lanes = []
        if self.lane < len(nearby_cars) - 1:
            allowed_lanes.append(self.lane + 1)
        if self.lane > 0:
            allowed_lanes.append(self.lane - 1)

        if prefer_right:
            allowed_lanes = reversed(allowed_lanes)

        for lane in allowed_lanes:
            if self.lane_is_safe(nearby_cars[lane], safety_distance):
                self.lane = lane
                return True
        return False

    def lane_is_safe(self, cars_in_lane, safety_distance):
        if not cars_in_lane:
            return True
        distances = [abs(car.position - self.position) for car in cars_in_lane]
        return min(distances) > safety_distance
