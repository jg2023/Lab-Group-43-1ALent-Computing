from floodsystem.utils import sorted_by_key

def stations_level_over_threshold(stations,tol):
    list = []
    for station in stations:
        try:
            relative = station.relative_water_level()
            if relative>tol:
                list.append((station,relative))
        except:
            print("Unknown error for station: {station}")
    if len(list)>0:
        list = sorted_by_key(list,1,True)
    else:
        list = []
    return list

def stations_highest_rel_level(stations,N):
    List = []
    for station in stations:
        relative_level = station.relative_water_level()
        List.append((station,relative_level))
    List = sorted_by_key(List,1,True)
    print(List)
    return List[:N]