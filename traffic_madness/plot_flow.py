import matplotlib.pyplot as plt
import numpy as np
from traffic_madness.config import Config
from os import listdir
import re

def plot_flow():
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
            # plt.plot(data[:, 0], data[:, 1], label='Flow {:.2f}'.format(aggressives))
            plt.scatter(aggressives, flow, c='k')
            maxi = max(data[:, 1])
            mini = min(data[:, 1])
            plt.scatter(aggressives, mini + (maxi - mini) / 2, c='b')
            plt.plot([aggressives, aggressives], [max(data[:, 1]), min(data[:, 1])], 'k-')
    plt.scatter([], [], c='k', label='Average flow')
    plt.scatter([], [], c='b', label='Middle of fluctuation')
    plt.plot([], [], 'k-', label='Fluctuation')
    # file = 'data/flow_aggressives_100cars/aggressives0.09.dat'
    # data = np.loadtxt(file)
    # flow = np.average(data[:, 1])
    # plt.scatter(0.09, flow, c='k')
    # plt.plot(data[:, 0], data[:, 1], label='Flow')
    plt.legend(loc='best')
    plt.xlabel('Ratio of aggressive drivers')
    plt.ylabel('traffic flow / optimal traffic flow')
    plt.show()

plot_flow()