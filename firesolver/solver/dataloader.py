from re import I
import pandas as pd
import numpy as np

_data_frame_dict = {}

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


def load_csv():
    paths = map(lambda name: "data/{}.csv".format(name), _csv_names)
    for path, name in zip(paths, _csv_names):
        _data_frame_dict[name] = pd.read_csv(path).to_numpy()

    normalize_names = [
        "average_foliage_density",
        "average_predic_temp",
        "average_rainfall",
        "unit_arson_report",
        "unit_camping_traffic",
        "unit_firework_sales",
    ]
    for name in normalize_names:
        norm_factor = 1 / np.amax(_data_frame_dict["average_rainfall"])
        _data_frame_dict[name] = np.multiply(_data_frame_dict[name], norm_factor)


def get_data(data_name: str):
    if len(_data_frame_dict) == 0:
        load_csv()

    return _data_frame_dict[data_name]


if __name__ == "__main__":
    print(get_data("average_rainfall"))
