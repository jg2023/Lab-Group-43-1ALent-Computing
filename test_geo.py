"""Unit test for the geo module"""

from numpy import sort
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from haversine import haversine

from floodsystem.utils import sorted_by_key

def test_rivers_by_distance():
    """This function tests the function used in 1B"""
    stations = build_station_list()
    p = 52.2053, 0.1218
    for station in stations:
        coords = station.coord
        assert coords
        assert coords == station.coord
        distance = haversine(p, station.coord)
        tuples.append((station.name, distance))
    tuples = sorted_by_key(tuples, 1)
    closest = tuples[0]
    assert closest == 0.840237595667494
    assert type(closest) == float
    assert len(coords) == len(stations)