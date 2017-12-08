import matplotlib.pyplot as plt
import numpy as np
from traffic_madness.config import Config

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


file = 'data/flow_aggressives_100cars/aggressives0.00.dat'
data = np.loadtxt(file)
flow = np.average(data[:, 1])
plt.scatter(0.0, flow, c='k')
# plt.plot(data[:, 0], data[:, 1], label='Flow')
plt.legend(loc='best')
plt.xlabel('time [s]')
plt.ylabel('traffic flow [cars / h]')
# plt.ylim(5000, 8000)
plt.show()


def optimal_flow(aggressives):
    config = Config()
    (config.speed_limit / config.track_length)