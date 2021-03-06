from re import I
import pandas as pd
import numpy as np
import sys

_data_frame_dict = {}
_norm_data_frame_dict = {}
#  all csv names
_csv_names = [
    "average_foliage_density",
    "average_pop_density",
    "average_predic_temp",
    "average_rainfall",
    "Fire_Station_Locations",
    "Key_Site_Locations",
    "map_water",
    "unit_arson_report",
    "unit_camping_traffic",
    "unit_firework_sales",
]


# names that make sense to normalize
# for example we do not include the map water data
_normalize_names = [
    "average_foliage_density",
    "average_predic_temp",
    "average_rainfall",
    "unit_arson_report",
    "unit_camping_traffic",
    "unit_firework_sales",
]


def load_csv():
    """
    load_csv: function to load all csv files. We also normalize the data being ingested right off the bat.
    storing the results as globals
    """ 
    # read files, tracking smallest dimensions
    smallest_rows = sys.maxsize
    smallest_cols = sys.maxsize
    paths = map(lambda name: "data/{}.csv".format(name), _csv_names)
    for path, name in zip(paths, _csv_names):
        _data_frame_dict[name] = pd.read_csv(path).to_numpy()
        rows, cols = _data_frame_dict[name].shape

        if rows < smallest_rows:
            smallest_rows = rows
        if cols < smallest_cols:
            smallest_cols = cols

    # clip data to smallest size
    print("original shape", smallest_rows, "x", smallest_cols)
    for name in _csv_names:
        _data_frame_dict[name] = np.resize(
            _data_frame_dict[name], (smallest_rows, smallest_cols)
        )

    # store normalized versions of data
    for name in _normalize_names:
        _norm_data_frame_dict[name] = normalize_data(_data_frame_dict[name])


def normalize_data(data):
    """
    normalize_data: helper fucntion to normalize data.
    :param data: takes in a M x N matrix of raw data from the provided csv
   
    :return: the statistically significant areas based on the z_threshold
    """ 
    # normalize respective data between 0 and 1
    norm_factor = 1 / np.amax(data, where=~np.isnan(data), initial=0)
    return np.multiply(data, norm_factor)


def get_data(data_name: str):
    """
    get_data: helper fucntion to laod the data.
    :param data: takes in a M x N matrix of raw data from the provided csv
    :return: loaded data
    """ 
    if len(_data_frame_dict) == 0:
        load_csv()

    return _data_frame_dict[data_name]


def get_norm_data(data_name: str):
    if len(_norm_data_frame_dict) == 0:
        load_csv()

    return _norm_data_frame_dict[data_name]


if __name__ == "__main__":
    print(get_data("average_rainfall"))
