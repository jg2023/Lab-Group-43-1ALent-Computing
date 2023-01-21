from floodsystem import geo
from floodsystem import stationdata

def run():
    stations = stationdata.build_station_list()
    centre = 52.2053, 0.1218
    r = 10
    stations_within_radius = geo.stations_within_radius(stations, centre, r)
    return print("Within r from centre: ", stations_within_radius)

if __name__ == "__main__":
    run()