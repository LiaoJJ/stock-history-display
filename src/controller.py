import matplotlib.pyplot as plt
import time
import glob
import sys
import os
from src.history_data_processor import process_history, get_default_history_data
from src.stock_data_loader import get_stock_data
from src.profit_segment_converter import history2profit_segment, profit_segment_list2str
from src.my_plot import my_plot
from src.profit_segment_converter import profit_segment2statistics, profit_segment_list2str
import random

def process(history_data, stock_abbr ='TSLA', period ='1y', filter_profit = 10, rand = str(random.random())):
    interval = '1d'

    # Get or download stock_data
    data = get_stock_data(stock_abbr, period, interval)["Average"]

    # Process history data
    history = process_history(history_data)
    last = [data.index[-1], 0, 0, 0, data[data.index[-1]]]
    profit_segment = history2profit_segment(history, last)
    print(profit_segment_list2str(profit_segment))
    my_plot(data, profit_segment, stock_abbr, period, filter_profit, rand)
    profit_segment_statistics = profit_segment2statistics(profit_segment)
    profit_segment_str = profit_segment_list2str(profit_segment)

    return profit_segment_statistics+"\n"+profit_segment_str

process(history_data=get_default_history_data("TSLA"))
