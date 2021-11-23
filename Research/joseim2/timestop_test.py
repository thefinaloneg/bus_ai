#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import requests
import csv
import key
import time
import time_handler
import arrive
import stop_id
import csv_handler
# increase cell width
from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))

def main():
    bulk_difference("IU:1", 4)

if __name__ == "__main__":
    main()


url = "https://developer.cumtd.com/api/v2.2/json/getdeparturesbystop?key=" + key.get_key() + "&stop_id=iu:1&count=5"
payload= {}
headers = {}
response = requests.request("GET", url, headers=headers, data=payload)

print(response.json()["time"])
print(response.json()["departures"][0]["stop_id"])
print(response.json()["departures"][0]["headsign"])
print(response.json()["departures"][1]["trip"]["direction"])
print(response.json()["departures"][0]["location"])
print("Sceduled: " + str(response.json()["departures"][1]["scheduled"]))
print("Expected: " + str(response.json()["departures"][1]["expected"]))
print(str(response.json()["departures"][1]["expected_mins"]) + " mins")

# Outcome of whether current several buses came before or after the scheduled or expected time -> 3 for scheduled, 4 or expected
def bulk_difference(stop_id, sc_ex):
    results = []
    bus_headsign = arrive.arrival_queue(stop_id)
    if bus_headsign is False:
        print(stop_id + " does not exist.")
        return
    csv_handler.start_csv()
    for i in range(0, 20): # change depending on how many departures want to be monitored, will run consecutively as a queue for each departure
        bus_headsign = arrive.arrival_queue(stop_id)
        original_expected = stop_id.stop_id_info(stop_id) # this checks to see if there are departures
        if original_expected is False:
            print("No departures anytime soon for " + stop_id + ".")
            return
        try:
            original_expected = stop_id.stop_id_info(stop_id)[bus_headsign[0]][4]
            current_routeid = stop_id.stop_id_info(stop_id)[bus_headsign[0]][0]
        except KeyError:
            break
        while (True):
            if arrive.arrival_queue(stop_id)[0] != bus_headsign[0]:
                if len(results) != 0: # accounts for buses that arrive before the range, improbable but did happen
                    csv_handler.append_csv(stop_id, bus_headsign[0], current_routeid, time_handler.time_converter(original_expected, "soft"), str(results[len(results) - 1]))
                    print('Arrived at: ' + str(results[len(results) - 1]))
                    break
                else: # eliminate this whole block later, was made for this particular print
                    print('Arrived at: ' + int(time_handler.time_difference(stop_id, bus_headsign[0], sc_ex, original_expected)))
                    csv_handler.append_csv(stop_id, bus_headsign[0], current_routeid, time_handler.time_converter(original_expected, "soft"), str(results[len(results) - 1]))
                    break
            if -120 <= int(time_handler.time_difference(stop_id, bus_headsign[0], sc_ex, original_expected)) and int(time_difference(stop_id, bus_headsign[0], sc_ex, original_expected)) <= 300:
                print("Current time difference: " + str(time_handler.time_difference(stop_id, bus_headsign[0], sc_ex, original_expected)))
                print("Expected time: " + original_expected + "\n")
                results.append(int(time_handler.time_difference(stop_id, bus_headsign[0], sc_ex, original_expected)))
                time.sleep(3)
            else:
                print("Time until next bus arrives: " + str(time_handler.time_difference(stop_id, bus_headsign[0], sc_ex, original_expected)))
                print("Expected time: " + original_expected + "\n")
                results.append(int(time_handler.time_difference(stop_id, bus_headsign[0], sc_ex, original_expected)))
                time.sleep(30)
    print(results)

#  Monitor first three in the queue


import folium
map = folium.Map(location=[40.10051, -88.222833], zoom_start = 11, tiles = 'cartodbpositron')
map
# https://vega.github.io/vega/examples/time-units/
# https://altair-viz.github.io/index.html


# CSV Format: stop_id | bus_headsign | route_id | expected_time | true_time

# At the start of the code:
with open("../joseim2/bus_data.csv", "wt") as f:
    filewriter = csv.writer(f, delimiter=",")
    filewriter.writerow(["stop_id", "bus_headsign", "route_id", "expected_time", "true_time"])

# To append to this same CSV:
with open("../joseim2/bus_data.csv", "a") as f:
    filewriter = csv.writer(f, delimiter=",")
    filewriter.writerow(["IU:1", "220N Illini", "100 YELLOW", "15:36:19", "15:37:23"])


# Changes to be done:
# Code is not running properly when the stop doesn't have any expected departures.
# Check for any index errors that might occur, like in the result break.
# We need to maintain the original expected time so we can get the real result.

response = requests.get("https://developer.cumtd.com/api/v2.2/json/getdeparturesbystop?key=" + key.get_key() + "&stop_id=" + 'WDSR:2')
if response.json()["departures"] == []:
    print('This stop has no departures.')
else:
    print('Passing here')
    response.json()

response = requests.get("https://developer.cumtd.com/api/v2.2/json/getdeparturesbystop?key=" + key.get_key() + "&stop_id=" + 'PLAZA')
response.json()





