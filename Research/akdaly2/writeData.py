# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import requests
import csv
from time import time, sleep
import time
### enter your own API key
url = "https://developer.cumtd.com/api/v2.2/json/getdeparturesbystop?key==user_key&stop_id=iu&count=10"
header = [" curr_time ", " stop_id ", " bus_num(headsign) ", " scheduled_time ", " expected_time ", " expected_mins "]
payload = {}
headers = {}


# %%
### writes data into a CSV 
### Need to put r in front of link in order for function to read data.
### Ex: writeData(r"C:Users\user\place", int(time.time()), int(time.time() + 30), 3)
def write_data(link, start_time, end_time, gap):
    ### creating the writer
    f = open(link, "w", encoding = "UTF8", newline = '')
    writer = csv.writer(f)
    writer.writerow(header)
    for _ in range(start_time, end_time, gap):
        ### stops function from running for gap seconds
        sleep(gap)
        ### need to request every gap seconds to get current data
        response = requests.request("GET", url, headers=headers, data=payload)
        ### writing the data (note that they are in brackets otherwise csv will interpret strings as a list)
        writer.writerow([response.json()["time"]] +
        [response.json()["departures"][0]["stop_id"]] +
        [response.json()["departures"][0]["headsign"]] +
        [response.json()["departures"][1]["trip"]["direction"]] + 
        [response.json()["departures"][1]["scheduled"]] +
        [response.json()["departures"][1]["expected"]] +
        [response.json()["departures"][1]["expected_mins"]])
    f.close()