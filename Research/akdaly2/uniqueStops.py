import pandas as pd
import csv
import os
df = pd.read_csv (r'C:\Users\ad120\OneDrive\Group56-FA21\Research\akdaly2\stops.txt')
with open(r'C:\Users\ad120\OneDrive\Group56-FA21\Research\akdaly2\stops.txt') as f:
    s = f.read() + "\n"
lines = s.split("\n")
stops = set()
pretty_stops = set()
for line in range(1, len(lines)):
    try:
        values = lines[line].split(",")[3]
        stop = values.split(":")[0]
        pretty_stop = lines[line].split(",")[7].split("(")[0]
        stops.add(stop)
        pretty_stops.add(pretty_stop)
    except:
        pass