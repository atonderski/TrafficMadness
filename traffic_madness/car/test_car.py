from traffic_madness.car.simple_car import SimpleCar
import matplotlib.pyplot as plt
import matplotlib.animation as animation

car = SimpleCar(5, 4, 1)
car2 = SimpleCar(6, 3, 1)
car3 = SimpleCar(3, 2, 1)
cars = [car, car2, car3]
print(car.velocity)

def update(frames):
    car.update(7, cars)
    car2.update(7, cars)
    car3.update(7, cars)
    line, = plt.scatter([car.position for car in cars])
    return line,

def init():
fig, ax = plt.subplot()