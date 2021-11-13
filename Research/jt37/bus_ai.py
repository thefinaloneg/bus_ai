#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
import time
import key

# Converts "T-notation time" into seconds from 00:00
def time_converter(time):
    yes = time.split("T")
    no = yes[1].split("-")
    no1 = str(no[0]).split(":")
    return int(no1[1]) * 60 + int(no1[2])

# Gives the actual time of bus arrival with parameters being a bus name and a bus stop

def actualtime(bus_name, bus_stop):
    url = "https://developer.cumtd.com/api/v2.2/json/getdeparturesbystop?key=" + key.get_key() + "&stop_id="     + bus_stop + "&count=15"
    response = requests.request("GET", url, headers=headers)
    list1 = []
    
    # Creates a list of bus names to iterate through and look for desired bus
        
    for i in range(0, 15):
        list1.append(str(response.json()["departures"][i]["headsign"]))

    # Restarts requests after 2 minutes if not within the first 15 buses that will arrive
        
    while (bus_name not in list1):
        time.sleep(120)
    
    index = list1.index(bus_name)
    
    # Narrows down which bus is being tracked and prevents code from proceeding until it is within 2 minutes of arrival
    while response.json()["departures"][index + 1]["expected_mins"] > 2:
        time.sleep(30)
        response = requests.request("GET", url, headers=headers)
        
        # Tracks down when the bus is within 10 seconds of estimated time of arrival,
        # pausing every 5 seconds if it's not, and refreshing
        
    while (time_converter(str(response.json()["time"])) -            time_converter(str(response.json()["departures"][index + 1]["expected"])) < 10):
        time.sleep(5)
        response = requests.request("GET", url, headers=headers, data=payload)
        
    # returns the now expected time, which is extremely accurate to the actual time arrival
    
    return response.json()["departures"][index + 1]["expected"]

# finds a specific bus to track down all the stops it goes to, with
# the bus name to be tracked as a parameter

def recordbus(bus_name):
    url = "https://developer.cumtd.com/api/v2.2/json/getvehicles?key=" + key.get_key()
    response = requests.request("GET", url, headers=headers)
    current_stop = ""
    
    # stop for the final destination
    
    destination = ""
    
    # checks if the bus line is operative or not
    
    exist = False
    
    # keeps track of which vehicle is being examined
    
    vehicle_id = ""
    
    # Runs until the bus the user requests for is active
    
    while(exist == False):
        for i in range(1, 30):
            if response.json()[vehicles][i][route_id] == bus_name:
                current_stop = response.json()[vehicles][i][trip][origin_stop_id]
                destination = response.json()[vehicles][i][trip][destination_stop_id]
                vehicle_id = response.json()[vehicles][i][vehicle_id]
                exist = True
                
    # Iterates through the bus system like a linked list, setting the stop to keep track of 
    # as the next one after the current stop is evaluated
    
    url = "https://developer.cumtd.com/api/2.2/json/getvehicle?key=" + key.get_key()     + vehicle_id
    response = requests.request("GET", url, headers=headers)
    while response.json()[vehicles][next_stop_id] != destination:
        with open("bus_output.txt","a") as f:
            f.write("{},{},{},{},{} \n".format(bus_name, direction, current_stop, route_id, actualtime(bus_name, current_stop)))
            current_stop = response.json()[vehicles][next_stop_id]
            
    # runs one final time on the final destination stop
            
    with open("bus_output.txt","a") as f:
        f.write("{},{},{},{},{} \n".format(bus_name, direction, destination, route_id, actualtime(bus_name, current_stop)))
    


# In[ ]:




