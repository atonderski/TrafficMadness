import matplotlib.pyplot as plt
import numpy as np
from traffic_madness.config import Config
from os import listdir
import re


def plot_flow():
    colors = ['k', 'b', 'r']
    # Path were to find the data that is wanted to be ploted
    path = 'data/test/'
    # Gives a list of files at that path
    files = listdir(path)

    for file in files:
        # Do not try to plot the config file
        if file != 'config.py':
            data = np.loadtxt(path + file)
            if re.findall("before", file):
                color_index = 0
            elif re.findall("after", file):
                color_index = 1
            elif re.findall("final", file):
                color_index = 2

            # Get the average flow over all observation time
            flow = np.average(data[:, 1])
            # Get the number of aggressive drivers from the filename
            aggressives = float(re.findall("\d+\.\d+", file)[0][:])
            # Plot the flow's time dependence
            # plt.plot(data[:, 0], data[:, 1],
            #          label='Flow {:.2f}'.format(aggressives))
            # Plot one data point with the averaged flow depending on
            # proportion of aggressive drivers
            plt.scatter(aggressives, flow, c=colors[color_index])

            ''' Plot binned flow '''
            # data_x = []
            # data_y = []
            # buckets = 10
            # buckets_length = int(len(data[:, 0]) / buckets)
            # for i in range(0, buckets):
            #     data_x.append(np.average(data[buckets_length * i : buckets_length * (i + 1), 0]))
            #     data_y.append(np.average(data[buckets_length * i: buckets_length * (i + 1), 1]))
            # plt.plot(data_x, data_y, 'r-')

            # Plot fluctuations for an estimate on reliability of data
            # maxi = max(data[:, 1])
            # mini = min(data[:, 1])
            # Data point in the middle of fluctuations
            # plt.scatter(aggressives, mini + (maxi - mini) / 2, c='b')
            # "Error bar"
            # plt.plot([aggressives, aggressives],
            #          [max(data[:, 1]), min(data[:, 1])], 'k-')

    # # Do same for second directory
    # # Path were to find the data that is wanted to be ploted
    # path = 'data/flow_aggressives_100niceCars/'
    # # Gives a list of files at that path
    # files = listdir(path)
    #
    # for file in files:
    #     # Do not try to plot the config file
    #     if file != 'config':
    #         data = np.loadtxt(path + file)
    #         # Get the average flow over all observation time
    #         flow = np.average(data[:, 1])
    #         # Get the number of aggressive drivers from the filename
    #         aggressives = float(re.findall("\d+\.\d+", file)[0][:])
    #         # Plot the flow's time dependence
    #         plt.plot(data[:, 0], data[:, 1],
    #                  label='Flow {:.2f}'.format(aggressives))
    #         # Plot one data point with the averaged flow depending on
    #         # proportion of aggressive drivers
    #         plt.scatter(aggressives, flow, c='k')
    #
    #         # Plot fluctuations for an estimate on reliability of data
    #         maxi = max(data[:, 1])
    #         mini = min(data[:, 1])
    #         # Data point in the middle of fluctuations
    #         plt.scatter(aggressives, mini + (maxi - mini) / 2, c='k', marker='d')
    #         # "Error bar"
    #         plt.plot([aggressives, aggressives],
    #                  [max(data[:, 1]), min(data[:, 1])], 'k-')


    # Empty opjects to generate the labels for the plots (else there would be
    # a label for every fiel)
    plt.scatter([], [], c='r', label='Average flow')
    plt.scatter([], [], c='r', marker='d', label='Middle of fluctuation')
    plt.plot([], [], 'r-', label='Fluctuation')
    plt.scatter([], [], c='k', label='Average flow nice cars')
    plt.scatter([], [], c='k', marker='d', label='Middle of fluctuation')
    plt.plot([], [], 'k-', label='Fluctuation')

    # Locate legend and plot axis labels
    plt.legend(loc='best')
    plt.xlabel('Ratio of aggressive drivers')
    plt.ylabel('traffic flow / optimal traffic flow')
    plt.show()


if __name__ == '__main__':
    plot_flow()
