import pygal
import time
from random import randrange
def random_list():
    rand_data = []
    for i in range(0, 36):
        rand_data.append(randrange(-2, 10))
    return rand_data
dot_chart = pygal.Dot(x_label_rotation=30)
dot_chart.title = "Illini Union"
times = []
for x in range(6, 24): 
    for y in range(0, 46, 30):
        if (y == 0):
            times.append(f"{x}:{y}0")
        else:
            times.append(f"{x}:{y}")
dot_chart.x_labels = times
dot_chart.add('220N', random_list())
dot_chart.add('220S', random_list())
dot_chart.add('1N', random_list())
dot_chart.add('1S', random_list())
dot_chart.add('13E', random_list())
dot_chart.add('13W', random_list())
dot_chart.render_to_file(r'C:\Users\ad120\OneDrive\Group56-FA21\Research\akdaly2\graphDemo.svg')
