from os.path import exists
import yfinance as yf
import pandas as pd

def calculate_average(data):
    avg_list = []
    for i in data.index:
        avg = (data["Open"][i]+data["High"][i]+data["Low"][i]+data["Close"][i])/4
        avg_list.append(avg)
    data["Average"] = avg_list

def get_stock_data(name, period, interval):
    # here this app will download the stock data to prevent duplicate download requests to Yahoo Finance.
    path_to_file = 'data/{}_{}.json'.format(name, period)
    file_exists = exists(path_to_file)
    if file_exists:
        data = pd.read_json(path_to_file)
    else:
        data = yf.download(name, period=period, interval = interval)
        calculate_average(data)
        data.to_json(path_to_file)
    return data
