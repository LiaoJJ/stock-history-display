import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np

line0=[[0,0], [1,1], [2,2]]
line1=[[0,0], [1, 1]]
line3=[[1,1],[2,2]]
segments = [line0, line1, line3]
colors = [(0, 0, 0, 1), (1, 0, 0, 1), (0, 1, 0, 1)]
offsets = [[0, 0],[0, -0.05],[0, 0.05]]

fig, ax = plt.subplots()
coll = LineCollection(segments, colors = colors, offsets=offsets)

ax.add_collection(coll)
ax.autoscale_view()

plt.show()
