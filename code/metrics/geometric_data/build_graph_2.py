import numpy as np
import os
import matplotlib.pyplot as plt
import math

# data_1 = np.random.normal(loc=(2, 0.5), scale=0.1, size=(n_data, 2))
# data_2 = np.random.normal(loc=(0, 0), scale=0.5, size=(n_data, 2))
# data = np.concatenate((data_1, data_2))
# np.save("data",data)
data = np.load("./data.npy")

x = data[:, 0]
y = data[:, 1]
plt.plot(x, y, "bo")


def connectpoints(x, y, p1, p2):
    x1, x2 = x[p1], x[p2]
    y1, y2 = y[p1], y[p2]
    plt.plot([x1, x2], [y1, y2], "k-")


# set the threshold and the distance type
threshold = 0.15
# choice of the distance type
# distance_type = "manhattan"
distance_type = "infinie"
# distance_type = "weighted manhattan"

for (i, j) in [(i, j) for i in range(0, x.shape[0]) for j in range(0, x.shape[0])]:
    # we look points a and b
    x_a = x[i]
    y_a = y[i]
    x_b = x[j]
    y_b = y[j]

    if distance_type == "manhattan":
        distance = abs(x_a - x_b) + abs(y_a - y_b)
    elif distance_type == "infinie":
        distance = max(abs(x_a - x_b), abs(y_a - y_b))
    elif distance_type == "weighted manhattan":
        distance = abs(x_a - x_b) + abs(y_a - y_b)
    if distance <= threshold:
        if i is not j:
            connectpoints(x, y, i, j)


file_name = f"images/thres_{threshold}_dist_{distance_type}.pdf"
plt.savefig(file_name)
plt.close()
