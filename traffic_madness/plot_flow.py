import matplotlib.pyplot as plt
import numpy as np

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

for i in range(0, 11):
    file = 'data/flow_aggressiveness%.2f.dat' % (0.1 * i)
    data = np.loadtxt(file)
    flow = np.average(data[:, 1])
    plt.scatter(0.1 * i, flow, c='k')

plt.legend(loc='best')
plt.xlabel('time [s]')
plt.ylabel('traffic flow [cars / h]')
# plt.ylim(5000, 8000)
plt.show()
