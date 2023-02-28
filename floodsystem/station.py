# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""

from floodsystem.datafetcher import fetch_latest_water_level_data
from . import datafetcher
import datetime
from tqdm import tqdm
from turtle import update

class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}\n".format(self.typical_range)
        return d
    
    def typical_range_consistent(self,advanced):

        if self.typical_range != None:
            if self.typical_range[0]<self.typical_range[1] and self.typical_range[0]>=0 and self.typical_range[1]>=0: 
                if not advanced:              
                    return True
                else:
                    dates,levels = datafetcher.fetch_measure_levels(self.measure_id,dt = datetime.timedelta(days = .5))
                    if len(dates) > 1 and len(levels)>1:
                        return True
        return False            

    def relative_water_level(self):
        low, high = self.typical_range[0], self.typical_range[1]
        if self.latest_level!=None:
            level = self.latest_level-low
            self.relative_level = level/(high-low)
            return self.relative_level
        print(f"No latest level found for station: {self.name}")
        self.relative_level = 0
        return 0
    
def inconsistent_typical_range_stations(stations,reverse = False,advanced = False):
    inconsistent_station_list = []
    consistent_station_list = []
    for station in tqdm(stations,desc = "Loading advanced inconsistent stations: "):
        A = station.typical_range_consistent(advanced=False)
        if not A:
            inconsistent_station_list.append(station.name)
        else:
            consistent_station_list.append(station)
    
    if not reverse:
        return inconsistent_station_list
    else:
        return consistent_station_list 

def set_relative_water_levels(stations):
    for station in tqdm(stations, desc = "Setting relative water levels"):
        station.relative_water_level()