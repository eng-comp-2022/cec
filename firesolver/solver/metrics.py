import dataloader
import numpy as np
from statsmodels.stats.weightstats import ztest as ztest
import math
import sys
import fire_resource_plan
# np.set_printoptions(threshold=sys.maxsize)


def grid_metrics():
    """
    grid metric. This calc the grid metric that is used the calculate the 
    probability of the fire in  a given location. This is based on a number of facters that 
    were provided .... rainfall, temp, firework etc. Along with some other metrics DMC and DC indexes.

    :return: M x N grid of probabilities
    """ 
    rain_data = dataloader.get_data("average_rainfall")
    foliage_data = dataloader.get_norm_data("average_foliage_density")
    temp = dataloader.get_norm_data("average_predic_temp")
    arson_report = dataloader.get_norm_data("unit_arson_report")
    camping_traffic = dataloader.get_norm_data("unit_camping_traffic")
    firework_sales = dataloader.get_norm_data("unit_firework_sales")

    DMC = dataloader.normalize_data(duff_moisture_content(rain_data))
    DC = dataloader.normalize_data(drought_code(rain_data))

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


def significant_areas(data, z_threshold=1):
    """
    significant areas: function to determine the sig.
    :param data: describe about parameter p1
    :param z_threshold: describe about parameter p2
    :return: the statistically significant areas based on the z_threshold
    """ 
    sample_mean = np.mean(data)
    sample_std = np.std(data)

    def z_score(sample):
        return (sample - sample_mean) / sample_std

    transform = np.vectorize(z_score)
    return transform(data) > z_threshold


def duff_moisture_content(ave_rainfall):
    """
    duff_moisture_content. Used in metric funct

    What is a Duff Moisture content?
    The Duff Moisture Code (DMC) is a numeric rating of the average moisture 
    content of loosely compacted organic layers of moderate depth.
    This code gives an indication of fuel consumption in moderate duff layers and medium-size woody material.
    ref: https://cwfis.cfs.nrcan.gc.ca/background/summary/fwi
    :param ave_rainfall: the average rainfall provided
    :return: the duff moisture index for the specific location
    """ 
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
    """
    drought code used in metric funct

    what is a drought code??
    The Drought Code (DC) is a numeric rating of the average moisture content of deep, 
    compact organic layers. This code is a useful indicator of seasonal drought effects on 
    forest fuels and the amount of smoldering in deep duff layers and large logs.
    ref: https://cwfis.cfs.nrcan.gc.ca/background/summary/fwi

    :param ave_rainfall: the average rainfall provided by the csv file 
    :return: the drought code index for the specific area 
    """ 
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
    # print("grid metrics:", grid_metrics())
    # print(rain_data())
    # print("SE:LRRRRRRRRJJJJj")
    # print(drought_code(rain_data()))
    # print(duff_moisture_content(rain_data()))
    s = significant_areas(grid_metrics())
    print(s[s == True].size)
    print(s.size)
