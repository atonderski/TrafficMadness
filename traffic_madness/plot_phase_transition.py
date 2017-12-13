import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from traffic_madness.config import Config
from os import listdir
import re
from mpl_toolkits import mplot3d
from matplotlib import cm

data = np.loadtxt('data/phases/phase-transition_3.dat',delimiter='\t',usecols=range(20))
print(data)

xlen=len(data[1,:])
ylen=len(data[:,1])
Xs = range(xlen)
Ys = range(ylen)
Xa, Ys = np.meshgrid(Xs, Ys)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(Xs,Ys,data, cmap=cm.coolwarm)
plt.show()
