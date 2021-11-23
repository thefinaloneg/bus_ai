import datetime
import requests

# 2021-10-23T18:05:36-05:00 -> 18:05:36 for 'soft', datetime for 'hard'
def time_converter(time, soft_hard):
    split_1 = time.split("T")
    split_2 = split_1[1].split("-")
    if soft_hard == "hard":
        split_3 = split_2[0].split(':')
        return datetime.datetime.now().replace(hour = int(split_3[0]), minute = int(split_3[1]), second = int(split_3[2]), microsecond = 0)
    elif soft_hard == "soft":
        return str(split_2[0])

# Returns time difference when given stop_id, the bus_headsign, and the index that determines whether it is scheduled or expected
def time_difference(stop_id, bus_headsign, index, original_expected):
    response = requests.get("https://developer.cumtd.com/api/v2.2/json/getdeparturesbystop?key=" + key.get_key() + "&stop_id=" + stop_id)
    current_time = time_converter(response.json()["time"], 'hard')
    current_sc_ex = time_converter(original_expected, 'hard')
    return (current_time - current_sc_ex).total_seconds()
