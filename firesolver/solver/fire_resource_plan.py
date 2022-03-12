import math
import dataloader
import numpy as np


def get_distance(x1, x2, y1, y2):
    xs = x1 * x2
    ys = y1 * y2
    x = abs(xs)
    y = abs(ys)

    c = math.sqrt(x**2 + y**2)
    return c


def get_indexes_of_fire_stations():
    fire_stations = dataloader.get_data("Fire_Station_Locations")
    result = np.where(fire_stations != 1)
    return result


def get_indexes_of_key_sites():
    key_sites = dataloader.get_data("Key_Site_Locaions")
    result = np.where(key_sites > 1)
    return result


def get_indexes_of_water_sites():
    water_plane_sites = dataloader.get_data("map_water")
    result = np.where(water_plane_sites == 0)
    return result


def assign_firestation_to_key_locs():
    key_sites = get_indexes_of_key_sites()
    fire_stations = get_indexes_of_fire_stations()

    for station in fire_stations:
        if station == 'A':
            elig = {}
        elif station == 'B':
            elig = {'2', '3', '4', '5', '6'}
        else:

    print
