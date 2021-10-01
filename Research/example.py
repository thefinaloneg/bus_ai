import requests

url = "https://developer.cumtd.com/api/v2.2/json/getdeparturesbystop?key={keys}&stop_id=iu&count=5"
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