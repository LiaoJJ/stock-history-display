import matplotlib.pyplot as plt
import time
import glob
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname("./"))
from history_data_processor import process_history, get_default_history_data
from stock_data_loader import get_stock_data
from algorithms import history2profit_segment
import random

def display(history_data, stock_abbr = 'TSLA', period = '1y', filter_profit = 10, rand = str(random.random())):
    interval = '1d'

    # Get or download stock_data
    data = get_stock_data(stock_abbr, period, interval)["Average"]

    # Process history data
    history = process_history(history_data)
    last = [data.index[-1], 0, 0, 0, data[data.index[-1]]]
    profit_segment = history2profit_segment(history, last)

    # plot picture
    plt.clf()
    fig, ax = plt.figure(figsize=(16, 9), dpi=120), plt.axes()
    # Plot adjusted close price my-history-data
    ax.plot(data, color='gray')
    for seg in profit_segment:
        if abs(seg[3]) <=filter_profit:
            continue
        offset = 3 if seg[3] > 0 else -3
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
    ax.text(data.index[1], max(data.values)-16, "Green = Earn", color='limegreen')
    ax.text(data.index[1], max(data.values)-32, "Red = Loss", color='r')

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
    time.sleep(0.05)

display(history_data=get_default_history_data("TSLA"))
