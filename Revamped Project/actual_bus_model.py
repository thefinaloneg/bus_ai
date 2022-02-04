import time
import requests
import key


def time_converter(time):
    yes = time.split("T")
    no = yes[1].split("-")
    no1 = str(no[0]).split(":")
    return int(no1[1]) * 60 + int(no1[2])


def find_vehicle_id(route_id):
    url = 'https://developer.cumtd.com/api/v2.2/json/getvehicles?key=' + key.get_key()
    response = requests.request("GET", url)
    for i in range(25):
        try:
            if route_id == response.json()["vehicles"][i]["trip"]["route_id"]:
                vehicle_id = response.json()["vehicles"][i]["vehicle_id"]
                return vehicle_id
        except Exception:
            print("This vehicle doesn't exist")


def bus_tracker(bus_id):
    url = 'https://developer.cumtd.com/api/v2.2/json/getvehicle?key=' + key.get_key() + '&vehicle_id=' + bus_id
    response = requests.request("GET", url)
    destination = response.json()["vehicles"][0]["destination_stop_id"]
    old_stop = response.json()["vehicles"][0]["next_stop_id"]
    timeout = time.time() + 60 * 60
    once_more = True
    while once_more:
        stop = response.json()["vehicles"][0]["next_stop_id"]
        while old_stop == stop:
            time.sleep(3)
            url = 'https://developer.cumtd.com/api/v2.2/json/getvehicle?key=' + key.get_key() + '&vehicle_id=' + bus_id
            response = requests.request("GET", url)
            stop = response.json()["vehicles"][0]["next_stop_id"]
            if time.time() > timeout:
                break
        print(old_stop)  # this needs to be converted into a write statement
        old_stop = stop
        if stop == destination:
            once_more = False
        if time.time() > timeout:
            break




if __name__ == '__main__':
    bus_tracker("1731")
