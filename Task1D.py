from floodsystem import geo
from floodsystem import stationdata

def run():
    stations = stationdata.build_station_list()
    rivers_with_station = geo.rivers_with_station(stations)
    print('First 10:',rivers_with_station[:10])

if __name__ == '__main__':
    run()

def run():
    stations = stationdata.build_station_list()
    stations_by_river = geo.stations_by_river(stations)
    print('River Aire:', stations_by_river['River Aire'], '\n')
    print('River Cam:', stations_by_river['River Cam'], '\n')
    print('River Thames: ', stations_by_river['River Thames'], '\n')

if __name__ == '__main__':
    run()