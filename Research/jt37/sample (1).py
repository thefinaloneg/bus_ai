#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests

keys = "cde8e82f02cb488daa290433126c745f"
url = "https://developer.cumtd.com/api/v2.2/json/getdeparturesbystop?key={}&stop_id=iu&count=5"
payload={}
headers = {}
response = requests.request("GET", url, headers=headers, data=payload)

print(response.json()["time"])
print(response.json()["departures"][0]["stop_id"])
print(response.json()["departures"][0]["headsign"])
print(response.json()["departures"][1]["trip"]["direction"])
print("Sceduled: " + str(response.json()["departures"][1]["scheduled"]))
print("Expected: " + str(response.json()["departures"][1]["expected"]))
print(str(response.json()["departures"][1]["expected_mins"]) + " mins")


#### curr_time, stop_id, bus_num(headsign), scehduled_time, expected_time, expected_mins
####  
####


# In[1]:


import time

def time_converter(time):
    yes = time.split("T")
    no = yes[1].split("-")
    no1 = str(no[0]).split(":")
    return int(no1[1]) * 60 + int(no1[2])

def actualtime(bus_name, bus_stop):
    url = "https://developer.cumtd.com/api/v2.2/json/getdeparturesbystop?key={}&stop_id=" + bus_stop + "&count=10" 
    response = requests.request("GET", url, headers=headers, data=payload)
    list1 = []
    for i in range(0, 10):
        list1.append(str(response.json()["departures"][i]["headsign"]))
    while bus_name not in list1 and final not True:
        return "This bus will not be arriving soon."
    else: 
        index = list1.index(bus_name)
    while response.json()["departures"][i + 1]["expected_mins"] > 2:
        time.sleep(30)
        response
    while (time_converter(str(response.json()["time"])) - time_converter(str(response.json()["departures"][i + 1]["expected"])) < 5):
        time.sleep(3)                                                    
        response                                                 
    return response.json()["departures"][i + 1]["expected"]

def recordbus():
    import datetime
    now = datetime.datetime.now()
    if now.day not in [1,2,3,18,19,20,21,22,23,24]:
        return "This bus does not run during these hours"
    url = "https://developer.cumtd.com/api/v2.2/json/getvehicles?key=cde8e82f02cb488daa290433126c745f"
    response = requests.request("GET", url, headers=headers, data=payload)
    stop = ""
    destination = ""
    final = False
    for (i in range(1, 30)):
        if response.json()[vehicles][i][route_id] == "ILLINI EVENING SATURDAY":
            stop = response.json()[vehicles][i][origin_stop_id]
            destination = response.json()[vehicles][i][destination_stop_id]
    while [vehicles][i][next_stop_id] != destination:
        with open("illini_evening_saturday_output.txt","a") as f:
            f.write("Something: {}".format(actualtime("ILLINI EVENING SATURDAY", stop)))
            stop = [vehicles][i][next_stop_id]
    final == true
    with open("illini_evening_saturday_output.txt","a") as f:
        f.write("Something: {}".format(actualtime("ILLINI EVENING SATURDAY", actualtime("ILLINI EVENING SATURDAY", destination))))
    


# In[ ]:




