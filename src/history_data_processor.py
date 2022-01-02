import calendar
import pandas as pd

def get_default_history_data(name):
    with open('data/{}.txt'.format(name)) as f:
        s = f.read().strip()
    return s

def process_history(input_string):
    data = []
    l = input_string.strip().replace("\r", "").replace("\n\n\n", "\n\n").split("\n\n")
    split = 1.0
    for row in l:
        if row.find('Canceled') != -1 or row.find("Dividend") != -1:
            continue
        if row.find("Split")!=-1:
            split = split_process(row, split)
            continue
        t = row.split('\n')
        cost = dollar_converter(t[2])
        time = time_converter(t[1])
        buy_sell = t[0].split(" ")[-1]
        volume = float(t[3].split(" ")[0]) * split
        unit_price = dollar_converter(t[3].split(" ")[3]) / split
        data.append([time, buy_sell, volume, cost, unit_price])

    data.reverse()
    # print(my-history-data)
    return data

def time_converter(date):
    m = {month: index for index, month in enumerate(calendar.month_abbr) if month}
    if date.find(",")!=-1:
        return pd.Timestamp(date)
    else:
        month = m[date.split(" ")[0]]
        day = int(date.split(" ")[1])
        return pd.Timestamp("2021-{:02d}-{:02d}".format(month, day))


def dollar_converter(cost):
    return float(cost[1:].replace(",", ""))

def split_process(str, split):
    return float(str.split("\n")[2].split(":")[0]) * split


# print(get_default_history_data("TSLA"))
