# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from floodsystem.stationdata import build_station_list
from .utils import sorted_by_key # noqa

from haversine import haversine

def stations_by_distance(stations, p):
    """Returns tuples with station name and distance from p"""
    stations = build_station_list()
    tuples = []
    for station in stations:
        coords = station.coord
        distance = haversine(p, station.coord)
        tuples.append((station.name, distance))
    tuples = sorted_by_key(tuples, 1)
    return tuples

def stations_within_radius(stations, centre, r):
    """Returns a list of stations within distance r from coordinate x"""
    stations = build_station_list()
    close_stations = []
    for station in stations:
        coords = station.coord
        radial_distance = haversine(centre, station.coord)
        if radial_distance < r:
            close_stations.append(station.name)
    close_stations.sort()
    return close_stations