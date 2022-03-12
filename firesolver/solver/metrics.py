import dataloader
import numpy as np


def grid_metrics():
    rain_data = dataloader.get_data("average_rainfall")
    return np.multiply(rain_data, 1.0)


def significant():
    pass
