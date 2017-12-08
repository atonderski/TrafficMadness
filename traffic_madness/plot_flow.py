import matplotlib.pyplot as plt
import numpy as np
from traffic_madness.config import Config
from os import listdir
import re

colors = ['k-', 'r-', 'b-', 'g-',
          'k--', 'r--', 'b--', 'g--',
          'k:', 'r:', 'b:', 'g:']
# plt.plot([], [], ' ', label='Proportion of aggressive drivers')
#
# for i in range(0, 11):
#     file = 'data/flow_aggressiveness%.2f_cars150.dat' % (0.1 * i)
#     data = np.loadtxt(file)
#     plt.plot(data[:, 0], data[:, 1], colors[i], label='%.2f' % (0.1 * i))
#
# plt.legend(loc='best')
# plt.xlabel('time [s]')
# plt.ylabel('traffic flow [cars / h]')
# plt.ylim(5000, 8000)
# plt.show()

files = listdir('data/flow_aggressives_100cars/')

for file in files:
    if file != 'config':
        data = np.loadtxt('data/flow_aggressives_100cars/' + file)
        flow = np.average(data[:, 1])
        aggressives = float(re.findall("\d+\.\d+", file)[0][:])
        plt.scatter(aggressives, flow, c='k')
# file = 'data/flow_aggressives_100cars/aggressives0.09.dat'
# data = np.loadtxt(file)
# flow = np.average(data[:, 1])
# plt.scatter(0.09, flow, c='k')
# plt.plot(data[:, 0], data[:, 1], label='Flow')
plt.legend(loc='best')
plt.xlabel('time [s]')
plt.ylabel('traffic flow [cars / h]')
plt.show()


def optimal_flow(aggressives):
    config = Config()
    (config.speed_limit / config.track_length)