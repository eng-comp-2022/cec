from cmath import inf
import math
from webbrowser import get
import dataloader
import numpy as np


def get_distance(x1, x2, y1, y2):
    xs = x1 - x2
    ys = y1 - y2
    x = abs(xs)
    y = abs(ys)

    c = math.sqrt(x**2 + y**2)
    return c

fire_stat = ['A', 'C', 'B']

def get_indexes_of_fire_stations():
    fire_stations = dataloader.get_data("Fire_Station_Locations")
    i = 0
    result =[]
    for i in range(len(fire_stations)):
        for j in range(len(fire_stations[i])):
            if(fire_stations[i][j] in fire_stat):
                result.append([i,j, fire_stations[i][j]])
   
    return result



def get_indexes_of_key_sites():
    key_sites = dataloader.get_data("Key_Site_Locations")
    i = 0
    result =[]
    for i in range(len(key_sites)):
        for j in range(len(key_sites[i])):
            if(key_sites[i][j] != None and key_sites[i][j] > 1):
                result.append([i,j, key_sites[i][j]])

    
    return result


def get_indexes_of_water_sites():
    water_site = dataloader.get_data("map_water")
    i = 0
    result =[]
    for i in range(len(water_site)):
        for j in range(len(water_site[i])):
            if(water_site[i][j] != None and water_site[i][j] == 0):
                result.append([i,j, water_site[i][j]])

    
    return result

def assign_firestation_to_key_locs():
    key_sites = get_indexes_of_key_sites()
    fire_stations = get_indexes_of_fire_stations()
    
    result = []
  
    for key_site in key_sites:
        min = 1000000
        min_coord = None

        for station in fire_stations:
          
            dist = get_distance(station[0], int(key_site[0]), station[1], int(key_site[1]))
         
            if min > dist:
                min = dist
                station_id = str(station[2]) +"_" + str(station[0]) +"_"+str(station[1])
                min_coord = {"station":[station[0], station[1], station[2]],"key_site":[key_site[0],key_site[1], key_site[2]],"station_id":station_id}
    
        result.append(min_coord)
 

    station_list =[]
    
    key_site_list_station = {2: [], 3: [], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[], 11:[], 12:[]}
    #  remove duplicates

    for site in key_site_list_station.keys():
        for entry in result:
            if entry["key_site"][2] == site and entry["station_id"] not in station_list:
                key_site_list_station[site].append(entry["station"])
                station_list.append(entry["station_id"])
    return key_site_list_station

def get_station_for_site(site_number):
    station_site_map = assign_firestation_to_key_locs()
    return station_site_map[site_number]
 

print(assign_firestation_to_key_locs()) 