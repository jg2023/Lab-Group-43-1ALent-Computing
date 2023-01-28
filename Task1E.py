from floodsystem import geo
from floodsystem import stationdata

def run():
    stations = stationdata.build_station_list()
    rivers_by_numbers_of_station = geo.rivers_by_station_number(stations,9)
    return print(rivers_by_numbers_of_station)

if __name__ == "__main__":
    run()