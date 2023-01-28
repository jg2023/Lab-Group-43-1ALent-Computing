from floodsystem.stationdata import build_station_list


def run():
    stations=build_station_list()
    for station in stations:
        if station.name in ['Bourton Dickler']:
            print(station.typical_range_consistent())

if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()