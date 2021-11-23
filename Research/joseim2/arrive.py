import key
import requests

# Returns a list of all buses, with different vehicle_id's, currently heading to this stop_id.
# When a bus leaves, they stop appearing in requests, and therefore the list everytime it's called.

def arrival_queue(stop_id):
    list = []
    response = requests.get("https://developer.cumtd.com/api/v2.2/json/getdeparturesbystop?key=" + key.get_key() + "&stop_id=" + stop_id)
    try:
        response.json()["departures"] # if "departures" does not exist, this stop doesn't exist either
    except KeyError:
        return False
    for i in range(0, len(response.json()["departures"])):
        if str(response.json()["departures"][i]["headsign"]) not in list: # Eliminating any dupes, leaving them for next time they're called
            list.append(str(response.json()["departures"][i]["headsign"]))
    print("Bus arrival queue: ")
    print(list)
    return list