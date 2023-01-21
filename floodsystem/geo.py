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
        distance = haversine(p, coords)
        tuples.append((station.name, distance))
    tuples = sorted_by_key(tuples, 1)
    return tuples

def stations_within_radius(stations, centre, r):
    """Returns a list of stations within distance r from coordinate x"""
    stations = build_station_list()
    close_stations = []
    for station in stations:
        coords = station.coord
        radial_distance = haversine(centre, coords)
        if radial_distance < r:
            close_stations.append(station.name)
    close_stations.sort()
    return close_stations

def rivers_with_station(stations):
    """Returns a list of rivers being monitored"""
    stations = build_station_list()
    rivers_monitored = set()
    for station in stations:
        rivers_monitored.add(station.river)
    rivers_monitored = sorted(rivers_monitored)
    return rivers_monitored

def stations_by_river(stations):
    """Returns a dictionary with river names as a key and a list of all the 
    station names on the respective river"""
    rivers = rivers_with_station(stations)
    river_dictionary = {}
    for river in rivers:
        river_dictionary[river] = [] #Generating Empty Dictionary with all river names
    for station in stations:
        river_dictionary[station.river].append(station.name) #Assigning values to each specific river
    return river_dictionary