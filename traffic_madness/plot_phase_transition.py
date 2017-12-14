import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from traffic_madness.config import Config
from os import listdir
import re
from mpl_toolkits import mplot3d
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d, Axes3D #<-- Note the capitalization! 

data = np.loadtxt('data/phases/phase-transition_2.dat',delimiter='\t',usecols=range(20))
print(data)

xlen=len(data[1,:])
ylen=len(data[:,1])
Xs = range(xlen)
Ys = range(ylen)
Xa, Ys = np.meshgrid(Xs, Ys)
fig = plt.figure()
#ax = plt.axes(projection='3d')
ax = Axes3D(fig)
ax.plot_surface(Xs,Ys,data,cmap=cm.coolwarm)
#ax.set_xlabel('xlabel')
#ax.set_ylabel('ylabel')
plt.show()
