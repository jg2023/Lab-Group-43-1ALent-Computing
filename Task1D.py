from floodsystem import geo
from floodsystem import stationdata

def run1D1():
    stations = stationdata.build_station_list()
    stations_by_river = geo.stations_by_river(stations)
    print('First 10:',stations_by_river[:10])

if __name__ == '__main__':
    run1D1()

def run1D2():
    stations = stationdata.build_station_list()
    stations_by_river = geo.stations_by_river(stations)
    print('River Aire:',stations_by_river['River Aire'])
    print('River Cam:',stations_by_river['River Cam'])
    print('River Thames: ',stations_by_river['River Thames'])

if __name__ == '__main__':
    run1D2()