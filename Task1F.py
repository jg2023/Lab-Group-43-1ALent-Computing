from floodsystem.stationdata import build_station_list
from floodsystem import station
from floodsystem.station import inconsistent_typical_range_stations

def run():
    stations=build_station_list()
    for station in stations:
        print(station.typical_range_consistent(advanced=False))

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()

from floodsystem.stationdata import build_station_list

def run():
    stations=build_station_list()
    print(inconsistent_typical_range_stations(stations))
    print(len(inconsistent_typical_range_stations(stations)))
    print(len(stations))

if __name__ == "__main__":
    run()
    