import dataloader
import numpy as np
from statsmodels.stats.weightstats import ztest as ztest
import math


def grid_metrics():
    rain_data = dataloader.get_data("average_rainfall")
    return np.multiply(rain_data, 1.0)


def significant_areas(data):
    alpha = 0.05
    _, p_vals = ztest(data, value=np.mean(data))
    return p_vals >= alpha


def Duff_Moisture_Content(ave_rainfall):

    DCM = np.empty(shape=(ave_rainfall.shape()))
    i = 0
    for x in ave_rainfall:
        j = 0
        for y in x:
            Pe = 0.92 * ave_rainfall[i, j]
            M = 1000
            DMC[i, j] = 244.72 - 43.43 * math.log(())


if __name__ == "__main__":
    # print(np.mean(grid_metrics()))
    print(significant_areas(grid_metrics()))
