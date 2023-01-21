"""Unit test for the geo module"""

from numpy import sort
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from haversine import haversine

from floodsystem.utils import sorted_by_key

def test_stations_by_distance():
    """This tests the function used in 1B"""
    stations = build_station_list()
    p = 52.2053, 0.1218
    tuples = []
    for station in stations:
        coords = station.coord
        distance = haversine(p, station.coord)
        tuples.append((station.name, distance))
    tuples = sorted_by_key(tuples, 1)
    closest = tuples[0]
    assert closest == 0.840237595667494
    assert type(closest) == float
    assert len(coords) == len(stations)

def test_stations_within_radius():
    """This tests the function used in 1C"""
    stations = build_station_list()
    centre = 52.2053, 0.1218
    r = 10
    close_stations = []
    for station in stations:
        coords = station.coord
        assert coords
        distance = haversine(centre, station.coord)
        if distance < r:
            close_stations.append(station.name)
    close_stations.sort()
    assert close_stations[0] == 'Bin Brook'