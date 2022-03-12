import dataloader
import numpy as np
from statsmodels.stats.weightstats import ztest as ztest
import math


def rain_data():
    rain_data = dataloader.get_data("average_rainfall")
    return np.multiply(rain_data, 1.0)


def grid_metrics():
    rain_data = dataloader.get_data("average_rainfall")
    foliage_data = dataloader.get_norm_data("average_foliage_density")
    temp = dataloader.get_norm_data("average_predic_temp")
    arson_report = dataloader.get_norm_data("unit_arson_report")
    camping_traffic = dataloader.get_norm_data("unit_camping_traffic")
    firework_sales = dataloader.get_norm_data("unit_firework_sales")

    DMC = dataloader.normalize_data(duff_moisture_content(rain_data))
    DC = dataloader.normalize_data(drought_code(rain_data))

    print("dmc", DMC)
    print("norm dmc", DC)

    metric = (
        np.multiply(foliage_data, 0.20)
        + np.multiply(temp, 0.28)
        + np.multiply(arson_report, 0.05)
        + np.multiply(camping_traffic, 0.06)
        + np.multiply(firework_sales, 0.06)
        + np.multiply(DMC, 0.20)
        + np.multiply(DC, 0.15)
    )
    return metric


def significant_areas(data, alpha=0.05):
    _, p_vals = ztest(data, value=np.mean(data))
    return p_vals >= alpha


#
def duff_moisture_content(ave_rainfall):
    def moisture_content_element(element):
        if element <= 1.5:
            return 0
        Pe = 0.92 * element - 1.27
        M_1 = 60
        M = (1000 * Pe / (48.77 + 0.9 * Pe)) + M_1
        if M <= 20:
            return 0
        # relative - no previous day's data
        # return 244.72 - 43.43 * math.log((M - 20))
        return 43.43 * math.log((M - 20))

    transform = np.vectorize(moisture_content_element)
    return transform(ave_rainfall)


def drought_code(ave_rainfall):
    def drought_code_element(element):
        Pe = 0.92 * element
        Q = 3.937 * Pe
        if Q == 0:
            return float("nan")
        if Q == 800:
            return 0
        return 400 * math.log((800 / Q))

    transform = np.vectorize(drought_code_element)
    dc = transform(ave_rainfall)

    # convert all nan values to maximum dc found
    nan_mask = np.isnan(dc)
    max_dc = np.amax(dc, where=~nan_mask, initial=0)
    dc[nan_mask] = max_dc
    return dc


if __name__ == "__main__":
    # print(np.mean(grid_metrics()))
    # print(significant_areas(grid_metrics()))
    print("grid metrics:", grid_metrics())
    # print(rain_data())
    # print("SE:LRRRRRRRRJJJJj")
    # print(drought_code(rain_data()))
    # print(duff_moisture_content(rain_data()))
