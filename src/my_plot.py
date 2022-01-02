import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np
import glob
import sys
import os

# line0=[[0,0], [1,1], [2,2]]
# line1=[[0,0], [1, 1]]
# line3=[[1,1],[2,2]]
# segments = [line0, line1, line3]
# colors = [(0, 0, 0, 1), (1, 0, 0, 1), (0, 1, 0, 1)]
# offsets = [[0, 0],[0, -0.05],[0, 0.05]]
#
# fig, ax = plt.subplots()
# coll = LineCollection(segments, colors = colors, offsets=offsets)
#
# ax.add_collection(coll)
# ax.autoscale_view()
#
# plt.show()


def my_plot(data, profit_segment, stock_abbr, period, filter_profit, rand):
    # plot picture
    plt.clf()
    x_size = ((int(period[0]) - 1) / 2 + 1) * 16
    y_size = 9
    fig, ax = plt.figure(figsize=(x_size, y_size), dpi=240), plt.axes()
    # Plot adjusted close price my-history-data
    ax.plot(data, color='gray')
    data_max = max(data.values)
    data_min = min(data.values)
    for seg in profit_segment:
        if abs(seg[3]) <= filter_profit:
            continue
        offset = (1 if seg[3] > 0 else -1) * (data_max - data_min) / 200
        color = 'limegreen' if seg[3] > 0 else 'r'
        label = "volume: {:.2f}, profit: {:.2f}".format(seg[2], seg[3])
        first_x = data[seg[0]:seg[1]].index[0]
        ax.annotate(label, (first_x, data[first_x]), color=color)
        ax.plot(data[seg[0]:seg[1]].add(offset), color=color)

    plt.ylabel('Price', fontsize=14)
    plt.xlabel('Time', fontsize=14)
    plt.title("Buy/sell History on %s" % stock_abbr, fontsize=16)
    plt.grid(which="major", color='dimgray', linestyle='-.', linewidth=0.5)
    fig.autofmt_xdate()
    ax.autoscale(tight=True)
    ax.text(data.index[1], data_max - 16, "Green = Earn", color='limegreen')
    ax.text(data.index[1], data_max - 32, "Red = Loss", color='r')

    # delete last pictures
    fileList = glob.glob('static/{}_{}_result_*.png'.format(stock_abbr, period))
    for filePath in fileList:
        try:
            os.remove(filePath)
        except:
            print("Error while deleting file : ", filePath)

    # save current picture
    # plt.show()
    picture_path = 'static/{}_{}_result_{}.png'.format(stock_abbr, period, rand)
    plt.savefig(picture_path)
    print("display success")
