# the time it says the bus will arrive vs. when it actually arrived

# check scheduled vs. expected time -> initial expected time difference
# then, send requests for current time as expected time gets closer to 0 --> -2 < 0 < 5
# if it goes beyond 5, stop sending requests, call this every 3 seconds

# bus scheduled and expected randomly get pushed back!!!

# add pt parameter, between route and count

# 2021-10-23T18:05:36-05:00 -> 18:05:36 for 'soft', datetime for 'hard'
import datetime
import requests
import time
import key
def time_converter(time, soft_hard):
    split_1 = time.split("T")
    split_2 = split_1[1].split("-")
    if soft_hard == "hard":
        split_3 = split_2[0].split(':')
        return datetime.datetime.now().replace(hour=int(split_3[0]), minute=int(split_3[1]), second=int(split_3[2]),
                                               microsecond=0)
    elif soft_hard == "soft":
        return str(split_2[0])


# Returns a list of all buses, with different vehicle_id's, currently heading to this stop_id.
# When a bus leaves, they stop appearing in requests, and therefore the list everytime it's called.
def arrival_queue(stop_id):
    list = []
    response = requests.get(
        "https://developer.cumtd.com/api/v2.2/json/getdeparturesbystop?key=" + key.get_key() + "&stop_id=" + stop_id)
    for i in range(0, len(response.json()["departures"])):
        if str(response.json()["departures"][i]["headsign"]) not in list:
            # Eliminating any dupes, leaving them for next time they're called
            list.append(str(response.json()["departures"][i]["headsign"]))
    print("Bus arrival queue: ")
    print(list)
    return list


#  key:'headsign', 0:'route_id', 1:'origin', 2:'destination', 3:'scheduled', 4:'expected',
#  5:'expected_mins', dictionary with info about current buses with same stop_id
def stop_id_info(stop_id):
    bus_dict = {}
    response = requests.get(
        "https://developer.cumtd.com/api/v2.2/json/getdeparturesbystop?key=" + key.get_key() + "&stop_id=" + stop_id)
    for i in range(0, len(response.json()["departures"])):
        if str(response.json()["departures"][i][
                   "headsign"]) not in bus_dict.keys():
            # Eliminating any dupes, leaving them for next time they're called
            bus_dict[str(response.json()["departures"][i]["headsign"])] = [
                str(response.json()["departures"][i]["route"]["route_id"]),
                str(response.json()["departures"][i]["origin"]["stop_id"]),
                str(response.json()["departures"][i]["destination"]["stop_id"]),
                str(response.json()["departures"][i]["scheduled"]), str(response.json()["departures"][i]["expected"]),
                str(response.json()["departures"][i]["expected_mins"])]
    return bus_dict


# Returns time difference when given stop_id, the bus_headsign,
# and the index that determines whether it is scheduled or expected
def time_difference(stop_id, bus_headsign, index):
    response = requests.get(
        "https://developer.cumtd.com/api/v2.2/json/getdeparturesbystop?key=" + key.get_key() + "&stop_id=" + stop_id)
    current_time = time_converter(response.json()["time"], 'hard')
    current_sc_ex = time_converter(stop_id_info(stop_id)[bus_headsign][index], 'hard')
    return -1 * (current_time - current_sc_ex).total_seconds()


# Outcome of whether current several buses came before or after the scheduled or expected time
# -> 3 for scheduled, 4 or expected
def bulk_difference(stop_id, sc_ex):
    results = []
    bus_headsign = arrival_queue(stop_id)
    response = requests.get(
        "https://developer.cumtd.com/api/v2.2/json/getdeparturesbystop?key=" + key.get_key() + "&stop_id=" + stop_id)
    for i in range(0, 1):
        original_expected = stop_id_info(stop_id)[bus_headsign[i]][4]  # try to integrate this into the code
        while True:
            try:
                value = int(time_difference(stop_id, bus_headsign[i], sc_ex))
                if arrival_queue(stop_id)[0] != bus_headsign[i]:
                    print('Break at: ' + str(results[len(results) - 1]))
                    break
            except KeyError:
                print('KeyError here')
                print('Break at: ' + str(results[len(results) - 1]))
                break
            if 120 >= int(time_difference(stop_id, bus_headsign[i], sc_ex)) and int(
                    time_difference(stop_id, bus_headsign[i], sc_ex)) <= 420:
                print("Current time difference: " + str(time_difference(stop_id, bus_headsign[i], sc_ex)))
                print("Expected time: " + stop_id_info(stop_id)[bus_headsign[i]][4] + "\n")
                results.append(int(time_difference(stop_id, bus_headsign[i], sc_ex)))
                time.sleep(5)
            else:
                print("Time until next bus arrives: " + str(time_difference(stop_id, bus_headsign[i], sc_ex)))
                print("Expected time: " + stop_id_info(stop_id)[bus_headsign[i]][4] + "\n")
                time.sleep(30)
    print(results)
    #with open("bus_output.txt", "a") as f:
        #f.write(results)


# Outcome of whether the bus came before or after the scheduled or expected time
def indiv_difference(headsign, stop_id, sc_or_ex):
    print('')


# print(time_difference('IU:1', '220N Illini Limited', 4))
bulk_difference('IU', 4)
