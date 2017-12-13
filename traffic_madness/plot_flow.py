import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from traffic_madness.config import Config
from os import listdir
import re


def plot_flow(path, marker='', label=['', '', '']):
    colors = ['b', 'k', 'r']
    # Path were to find the data that is wanted to be ploted
    # Gives a list of files at that path
    files = listdir(path)

    for file in files:
        # Do not try to plot the config file
        if file != 'config.py':
            data = np.loadtxt(path + file)
            if re.findall("before", file):
                continue
                # color_index = 0
            elif re.findall("after", file):
                continue
                # color_index = 1
            elif re.findall("final", file):
                # continue
                color_index = 1

            # Get the average flow over all observation time
            flow = np.average(data[:, 1])
            # Get the number of aggressive drivers from the filename
            aggressives = float(re.findall("\d+\.\d+", file)[0][:])
            # Plot the flow's time dependence
            # plt.plot(data[:, 0], data[:, 1],
            #          label='Flow {:.2f}'.format(aggressives))
            # Plot one data point with the averaged flow depending on
            # proportion of aggressive drivers
            plt.scatter(aggressives, flow, c=colors[color_index], marker=marker)

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

    # Empty opjects to generate the labels for the plots (else there would be
    # a label for every fiel)
    # plt.scatter([], [], c='b', marker=marker, label=label[0])
    plt.scatter([], [], c='k', marker=marker, label=label[1])
    # plt.plot([], [], 'r-', label='Fluctuation')
    # plt.scatter([], [], c='r', marker=marker, label=label[2])
    # plt.scatter([], [], c='k', marker='d', label='Middle of fluctuation')
    # plt.plot([], [], 'k-', label='Fluctuation')

    # Locate legend and plot axis labels




if __name__ == '__main__':
    matplotlib.rcParams.update({'font.size': 22})
    plot_flow(path = 'data/test/', marker='o', label=['85 Cars', '85 Cars', '85 Cars'])
    plot_flow(path='data/aggressives_500s_obs_150_cars/',
              marker='d', label=['150 Cars', '150 Cars', '150 Cars'])
    plot_flow(path='data/aggressives_500s_obs_200_cars/',
              marker='s', label=['200 Cars', '200 Cars', '200 Cars'])
    plt.plot([],[], 'white', label='Traffic flow, after one lane was blocked')
    plt.legend(loc='best')
    plt.xlabel('Ratio of aggressive drivers')
    plt.ylabel('Traffic flow / optimal traffic flow')

    plt.show()
