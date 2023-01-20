# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from floodsystem.stationdata import build_station_list
from .utils import sorted_by_key # noqa

import haversine

def stations_by_distance(stations, p):
    """This function creates tuples with station name and distance from p"""
    stations = build_station_list()
    tuples = []
    for station in stations:
        coords = station.coord
        distance = haversine(p, station.coord)
        tuples.append((station.name, distance))
    tuples = sorted_by_key(tuples, 1)
    return tuples