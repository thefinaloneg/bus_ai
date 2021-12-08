import pygal
dot_chart = pygal.Dot(x_label_rotation=30)
dot_chart.title = 'Buses'
dot_chart.add('Chrome', [6395, 8212, 7520, 7218, 12464, 1660, 2123, 8607])
dot_chart.add('Firefox', [7473, 8099, 11700, 2651, 6361, 1044, 3797, 9450])
dot_chart.add('Opera', [3472, 2933, 4203, 5229, 5810, 1828, 9013, 4669])
dot_chart.add('IE', [43, 41, 59, 79, 144, 136, 34, 102])
dot_chart.render_to_file(r'C:\Users\ad120\OneDrive\Group56-FA21\Research\akdaly2\visuals.svg')