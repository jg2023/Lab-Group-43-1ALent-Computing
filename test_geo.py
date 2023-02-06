"""Unit test for the geo module"""

from numpy import sort
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from haversine import haversine

from floodsystem.utils import sorted_by_key
from floodsystem import geo

def test_stations_by_distance():
    """This tests the function used in 1B"""
    stations = build_station_list()
    p = 52.2053, 0.1218
    stations_by_distance=geo.stations_by_distance(stations, p)
    closest=stations_by_distance[0]
    assert type(stations_by_distance)==list
    assert type(closest)==tuple
    assert type(closest[0])==str
    assert type(closest[1]) == float
    assert closest[1] == 0.840237595667494

def test_stations_within_radius():
    """This tests the function used in 1C"""
    stations = build_station_list()
    centre = 52.2053, 0.1218
    r = 10
    close_stations=geo.stations_within_radius(stations,centre,r)
    
    assert type(close_stations)==list
    assert close_stations[0] == 'Bin Brook'

def test_rivers_with_a_staion():
    """This tests the first function used in 1D"""
    stations=build_station_list()
    first_ten=geo.rivers_with_station(stations)[:10]
    assert type(first_ten)==list
    assert first_ten==['Addlestone Bourne', 'Aire Washlands', 'Alconbury Brook', 'Aldingbourne Rife', 'Aller Brook', 'Allison Dyke', 'Alverthorpe Beck', 'Ampney Brook', 'Amwell Loop', 'Arkle Beck']

def test_stations_by_river():
    """This tests the second function used in 1D"""
    stations=build_station_list()
    stations_by_river=geo.stations_by_river(stations)
    assert type(stations_by_river)==dict
    assert stations_by_river['River Aire']==['Airmyn', 'Apperley Bridge', 'Armley', 'Beal Weir Bridge', 'Bingley', 'Birkin Holme Washlands', 'Carlton Bridge', 'Castleford', 'Chapel Haddlesey', 'Cononley', 'Cottingley Bridge', 'Ferrybridge Lock', 'Fleet Weir', 'Gargrave', 'Gargrave High Street', 'Kildwick', 'Kirkstall Abbey', 'Knottingley Bank Dole Lock', 'Leeds Crown Point', 'Leeds Crown Point Flood Alleviation Scheme', 'Leeds Knostrop Weir Flood Alleviation Scheme', 'Oulton Lemonroyd', 'Saltaire', 'Snaygill', 'Stockbridge']
    assert stations_by_river['River Cam']==['Cam', 'Cambridge', 'Cambridge Baits Bite', 'Cambridge Jesus Lock', 'Dernford', 'Great Chesterford', 'Weston Bampfylde']
    assert stations_by_river['River Thames']==['Abingdon Lock', 'Bell Weir', 'Benson Lock', 'Boulters Lock', 'Bray Lock', 'Buscot Lock', 'Caversham Lock', 'Chertsey Lock', 'Cleeve Lock', 'Clifton Lock', 'Cookham Lock', 'Cricklade', 'Culham Lock', 'Days Lock', 'Ewen', 'Eynsham Lock', 'Farmoor', 'Godstow Lock', 'Goring Lock', 'Grafton Lock', 'Hannington Bridge', 'Hurley Lock', 'Iffley Lock', 'Kings Lock', 'Kingston', 'Maidenhead', 'Mapledurham Lock', 'Marlow Lock', 'Marsh Lock', 'Molesey Lock', 'Northmoor Lock', 'Old Windsor Lock', 'Osney Lock', 'Penton Hook', 'Pinkhill Lock', 'Radcot Lock', 'Reading', 'Romney Lock', 'Rushey Lock', 'Sandford-on-Thames', 'Shepperton Lock', 'Shifford Lock', 'Shiplake Lock', 'Somerford Keynes', 'Sonning Lock', 'St Johns Lock', 'Staines', 'Sunbury  Lock', 'Sutton Courtenay', 'Teddington Lock', 'Thames Ditton Island', 'Trowlock Island', 'Walton', 'Whitchurch Lock', 'Windsor Park']

def test_rivers_by_number_of_stations():
    """This tests the function used by 1E"""
    stations=build_station_list()
    most_popular_nine=geo.rivers_by_station_number(stations,9)
    assert len(most_popular_nine)>=9
    assert type(most_popular_nine)==list
    assert type(most_popular_nine[0])==tuple
    assert type(most_popular_nine[0][0])==str
    assert type(most_popular_nine[0][1])==int
    for i in range(len(most_popular_nine)-1):
        assert most_popular_nine[i][1]>=most_popular_nine[i+1][1]
