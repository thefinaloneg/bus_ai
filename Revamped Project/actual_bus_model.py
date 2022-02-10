import time
import requests
import key


def time_converter(time):
    yes = time.split("T")
    no = yes[1].split("-")
    no1 = str(no[0]).split(":")
    return int(no1[1]) * 60 + int(no1[2])


def find_vehicle_ids():
    url = 'https://developer.cumtd.com/api/v2.2/json/getvehicles?key=' + key.get_key()
    response = requests.request("GET", url)
    to_return = []
    for vehicle in response.json()["vehicles"]:
        to_return.append(vehicle["vehicle_id"])
    return to_return


def bus_tracker(bus_id, counter):
    url = 'https://developer.cumtd.com/api/v2.2/json/getvehicle?key=' + key.get_key() + '&vehicle_id=' + bus_id
    response = requests.request("GET", url)
    destination = response.json()["vehicles"][0]["destination_stop_id"]
    old_stop = response.json()["vehicles"][0]["next_stop_id"]
    route_id = response.json()["vehicles"][0]["trip"]["route_id"]
    time_to_return = response.json()["time"]
    timeout = time.time() + 60 * 60
    once_more = True
    while once_more:
        try:
            stop = response.json()["vehicles"][0]["next_stop_id"]
            while old_stop == stop:
                time.sleep(3)
                url = 'https://developer.cumtd.com/api/v2.2/json/getvehicle?key=' + key.get_key() + '&vehicle_id=' + bus_id
                response = requests.request("GET", url)
                stop = response.json()["vehicles"][0]["next_stop_id"]
                if time.time() > timeout:
                    break
            with open(f"bus{counter}.txt") as f:
                f.write(f"{route_id}, {old_stop}, {time_to_return}")
            old_stop = stop
            if stop == destination:
                once_more = False
            if time.time() > timeout:
                break
        except:
            with open(f"bus{counter}.txt") as f:
                f.write(f"{route_id}, {destination}, {time_to_return}")






if __name__ == '__main__':
    print(time.time())
