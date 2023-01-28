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

def rivers_by_station_number(stations, N):
    """Returns an ordered list of tuples of river names and the number of stations on 
    the river with length N (or larger to include all rivers with the same amount of 
    stations as the final river)"""
    unsorted_river_dictionary={}
    stations = build_station_list()
    station=stations_by_river(stations)
    list_of_stations=[]
    for i in range(len(station)): #Creates an unordered list of tuples of rivers and the number of stations
        list_of_stations.append((list(station)[i],len(list(station.values())[i])))
    list_of_stations.sort(key=lambda a: a[1],reverse=True) #Orders list
    truncated_list_of_stations=[]
    for i in range(N): #Truncates list to length N
        truncated_list_of_stations.append(list_of_stations[i])
    extra_elements=True
    i=N-1
    while extra_elements==True: #Adds any extra elements as needed
        if list_of_stations[i][1]==list_of_stations[i+1][1]:
            truncated_list_of_stations.append(list_of_stations[i+1])
            i+=1
        else:
            extra_elements=False
    return truncated_list_of_stations