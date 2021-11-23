import requests
import key

#  key:'headsign', 0:'route_id', 1:'origin', 2:'destination', 3:'scheduled', 4:'expected', 5:'expected_mins', dictionary with info about current buses with same stop_id

def stop_id_info(stop_id):
    bus_dict = {}
    response = requests.get("https://developer.cumtd.com/api/v2.2/json/getdeparturesbystop?key=" + key.get_key() + "&stop_id=" + stop_id)
    try:
        response.json()["departures"]
    except KeyError:
        return False
    for i in range(0, len(response.json()["departures"])):
        if str(response.json()["departures"][i]["headsign"]) not in bus_dict.keys(): # Eliminating any dupes, leaving them for next time they're called
            bus_dict[str(response.json()["departures"][i]["headsign"])] = [str(response.json()["departures"][i]["route"]["route_id"]), str(response.json()["departures"][i]["origin"]["stop_id"]), str(response.json()["departures"][i]["destination"]["stop_id"]), str(response.json()["departures"][i]["scheduled"]), str(response.json()["departures"][i]["expected"]), str(response.json()["departures"][i]["expected_mins"])]
    return bus_dict

