import matplotlib.pyplot as plt
import numpy as np

def __init(self,resolution,track):
    self.track = track
    self.resolution = resolution

alist = np.array([1,7,12,25,26])

def find_nearest(array,value):
    idx = (np.abs(array-value)).argmin()
    return array[idx]
      
def density(car_positions, track_length,resolution):
    X = np.linspace(0,track_length,resolution)
    Y = np.zeros(resolution)
    print(X)
    print(Y)
    for i in range(len(car_positions)):
        print(car_positions[i])
        nearest = find_nearest(X,car_positions[i])
        idx = list(X).index(nearest)
        Y[idx] = Y[idx] +1
        print(Y)
        norm = np.linalg.norm(Y)
        if (norm != 0):
            Y = Y / norm
    return Y

def showdensity(density):
    plt.plot(list(density))
    plt.ylabel('density')
    plt.show()

dens = density(alist,30,5)
showdensity(dens)
    
