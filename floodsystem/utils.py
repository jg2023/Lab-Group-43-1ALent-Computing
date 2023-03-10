# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains utility functions.

"""

import datetime
from numpy import sort
from tqdm import tqdm
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import update_water_levels
from floodsystem.station import set_relative_water_levels

def sorted_by_key(x, i, reverse=False):
    """For a list of lists/tuples, return list sorted by the ith
    component of the list/tuple, E.g.

    Sort on first entry of tuple:

      > sorted_by_key([(1, 2), (5, 1]), 0)
      >>> [(1, 2), (5, 1)]

    Sort on second entry of tuple:

      > sorted_by_key([(1, 2), (5, 1]), 1)
      >>> [(5, 1), (1, 2)]

    """

    # Sort by distance
    def key(element):
        return element[i]

    return sorted(x, key=key, reverse=reverse)

def fetch_station_list_levels(stations,dt,N):
	Stations = []
	erroneousStations = []
	stations = inconsistent_typical_range_stations(stations,True)
	for station in tqdm(stations, desc = "Loading: "):
		try:
			dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
			station.latest_level = levels[0]
			station.level_history = (dates,levels)
			Stations.append((station,station.latest_level-station.average_value))
		except:
			try:
				print(f"erroneous data for stations: {station.name}")
				erroneousStations.append(station)
			except:
				print('unknown error of',station)
	Stations = sorted_by_key(Stations,1,True)
	topStations = Stations[:N]
	j = N
	
	while len(topStations)<len(Stations) and(Stations[j-1][1] == Stations[j][1]):
		topStations.append(Stations[j])
		j+=1
	topNStations = []
	for i in topStations:
		topNStations.append(i[0])
	return topNStations

def assess_flood_risk(stations):
	update_water_levels(stations)
	set_relative_water_levels(stations)
	SevereThreshold = 1.1
	HighTheshold = 1.0
	MediumThreshold = 0.8
	LowThreshold = 0.6
	SevereRiskTowns = []
	HighRiskTowns = []
	MedRiskTowns = []
	LowRiskTowns = []
	for station in stations:
		if station.relative_level >= SevereThreshold:
			SevereRiskTowns.append((station.town,"Severe"))
		elif station.relative_level >= HighTheshold:
			HighRiskTowns.append((station.town,"High"))
		elif station.relative_level >= MediumThreshold:
			MedRiskTowns.append((station.town,"Medium"))
		elif station.relative_level >= LowThreshold:
			LowRiskTowns.append((station.town,"Low"))
	Towns =  SevereRiskTowns+HighRiskTowns+MedRiskTowns+LowRiskTowns
	return Towns