# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import csv
import os


# %%
df = pd.read_csv (r'C:\Users\ad120\OneDrive\Group56-FA21\Research\akdaly2\routes.txt')



# %%
with open(r'C:\Users\ad120\OneDrive\Group56-FA21\Research\akdaly2\routes.txt') as f:
    s = f.read() + "\n"
lines = s.split("\n")
routes = set()
for line in range(0, len(lines)):
    values = lines[line].split(",")
    routes.add(values[0])
    


