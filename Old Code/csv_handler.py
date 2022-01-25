import csv

def start_csv():
    with open("bus_data.csv", "wt") as f:
        filewriter = csv.writer(f, delimiter=",")
        filewriter.writerow(["stop_id", "bus_headsign", "route_id", "expected_time", "true_time"])

def append_csv(stop_id, bus_headsign, route_id, expected_time, true_time):
    with open("bus_data.csv", "a") as f:
        filewriter = csv.writer(f, delimiter=",")
        filewriter.writerow([stop_id, bus_headsign, route_id, expected_time, true_time])
