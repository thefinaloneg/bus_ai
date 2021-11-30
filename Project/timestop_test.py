#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import requests
import csv
import key
import time_difference
# increase cell width
from IPython.core.display import display, HTML

display(HTML("<style>.container { width:100% !important; }</style>"))


def main():
    time_difference.bulk_difference("IU:1", 4)


if __name__ == "__main__":
    main()

url = "https://developer.cumtd.com/api/v2.2/json/getdeparturesbystop?key=" + key.get_key() + "&stop_id=iu:1&count=5"
payload = {}
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

#  Monitor first three in the queue


import folium

map = folium.Map(location=[40.10051, -88.222833], zoom_start=11, tiles='cartodbpositron')
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

response = requests.get(
    "https://developer.cumtd.com/api/v2.2/json/getdeparturesbystop?key=" + key.get_key() + "&stop_id=" + 'WDSR:2')
if response.json()["departures"] == []:
    print('This stop has no departures.')
else:
    print('Passing here')
    response.json()

response = requests.get(
    "https://developer.cumtd.com/api/v2.2/json/getdeparturesbystop?key=" + key.get_key() + "&stop_id=" + 'PLAZA')
response.json()
