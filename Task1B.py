from floodsystem import geo
from floodsystem import stationdata

def run1B():
    stations = stationdata.build_station_list()
    p = 52.2053, 0.1218
    stations_by_distance = geo.stations_by_distance(stations,p)
    return print("Close: ", stations_by_distance[:10], "Far: ", stations_by_distance[-10:])

if __name__ == "__main__":
    run1B()