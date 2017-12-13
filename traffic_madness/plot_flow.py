import re
from os import listdir

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


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
            plt.scatter(aggressives, flow, c=colors[color_index],
                        marker=marker)

            ''' Plot binned flow '''
            # data_x = []
            # data_y = []
            # buckets = 10
            # buckets_length = int(len(data[:, 0]) / buckets)
            # for i in range(0, buckets):
            #     data_x.append(np.average(data[buckets_length * i :
            # buckets_length * (i + 1), 0]))
            #     data_y.append(np.average(data[buckets_length * i:
            # buckets_length * (i + 1), 1]))
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


def _plot_time_series(path):
    files = listdir(path)
    unique_series = [path + f.split('before.dat')[0] for f in files if
                     'before.dat' in f]
    unique_series.sort(reverse=True)
    velocity_factors = []
    for series_name in unique_series:
        velocity_factor = float(re.findall("\d+\.\d+", series_name)[1])
        # if velocity_factor not in [0.0, 0.3, 0.6, 1.0]:
        #     continue
        data_before = np.loadtxt(series_name + 'before.dat')
        data_after = np.loadtxt(series_name + 'after.dat')
        data_final = np.loadtxt(series_name + 'final.dat')
        last_time_before = max(data_before[:, 0])
        last_time_after = last_time_before + max(data_after[:, 0])
        time = np.concatenate((
            data_before[:, 0],
            data_after[:, 0] + last_time_before,
            data_final[:, 0] + last_time_after
        ))
        velocity = np.concatenate((data_before[:, 2],
                                   data_after[:, 2],
                                   data_final[:, 2]))
        plt.plot(time, velocity)
        velocity_factors.append(velocity_factor)
    plt.legend(velocity_factors)
    plt.plot((last_time_before, last_time_before), (0.4, 1), 'k--')
    plt.plot((last_time_after, last_time_after), (0.4, 1), 'k--')
    plt.title("Flow for different velocity awareness values")
    plt.xlabel("time (seconds)")
    plt.ylabel("velocity (relative to speed limit)")


def plot_traffic_flow():
    plt.figure(1)
    plot_flow(path='data/test/', marker='o',
              label=['85 Cars', '85 Cars', '85 Cars'])
    plot_flow(path='data/aggressives_500s_obs_150_cars/',
              marker='d', label=['150 Cars', '150 Cars', '150 Cars'])
    plot_flow(path='data/aggressives_500s_obs_200_cars/',
              marker='s', label=['200 Cars', '200 Cars', '200 Cars'])
    plt.plot([], [], 'white', label='Traffic flow, after one lane was blocked')
    plt.legend(loc='best')
    plt.xlabel('Ratio of aggressive drivers')
    plt.ylabel('Traffic flow / optimal traffic flow')


def plot_time_flow(path):
    plt.figure(2)
    _plot_time_series(path)


if __name__ == '__main__':
    matplotlib.rcParams.update({'font.size': 22})
    # plot_traffic_flow()
    plot_time_flow('data/tmp/')
    plt.show()
