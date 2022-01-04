import collections
import pandas as pd

# input (time, buy/sell, volume, total_cost, unit_price)
# output (start_time_string, end_time_string, volume, profit)
def history2profit_segment(A, last):
    n = len(A)
    cur = collections.deque()
    res = []
    i=0
    while i<n:
        t = A[i]
        if t[1]=="Buy":
            cur.append(t)
            i+=1
        else:
            if abs(cur[0][2]-t[2]) < 1e-7:
                profit = t[2] * (t[4] - cur[0][4])
                res.append([cur[0][0], t[0], t[2], profit, cur[0][4], t[4]])
                i += 1
                cur.popleft()
            elif cur[0][2]<t[2]:
                t[2] -= cur[0][2]
                profit = cur[0][2] * (t[4] - cur[0][4])
                res.append([cur[0][0], t[0], cur[0][2], profit, cur[0][4], t[4]])
                cur.popleft()
            elif cur[0][2]>t[2]:
                profit = t[2] * (t[4] - cur[0][4])
                res.append([cur[0][0], t[0], t[2], profit, cur[0][4], t[4]])
                cur[0][2] -= t[2]
                i += 1

    for c in cur:
        profit = c[2]*(last[4] - c[4])
        res.append([c[0], last[0], c[2], profit, cur[0][4], float('inf')])
    return res

def profit_segment_list2str(profit_segment):
    # print(profit_segment)
    def segment2str(A):
        temp = [str(A[0].date()), "{:.2f}".format(A[4]), str(A[1].date()), "{:.2f}".format(A[5]), "{:.2f}".format(A[2]), "{:.2f}".format(A[3])]
        return ", ".join(temp)
    return "profit_segment_list:\n[start_time, start_unit_price, end_time, end_unit_price, volume, profit]\n"+"\n".join([segment2str(a) for a in profit_segment])

def profit_segment2statistics(profit_segment):
    '''Metrics:
        - display total profit from the stock
        - display total transactions in this stock
        - max, avg, min hold days
        - max, avg, min profit statistics regarding the thread transactions'''
    volume = []
    profit = []
    hold_days = []
    n = len(profit_segment)
    for seg in profit_segment:
        hold_days.append((seg[1] - seg[0]).days)
        volume.append(seg[2])
        profit.append(seg[3])

    return '''Metrics:
        - total profit: {:.2f}
        - total thread transactions: {}
        - hold days: max={}, avg={}, min={} 
        - volume: max={}, avg={}, min={} 
        - profit: max={}, avg={}, min={} 
        '''.format(sum(profit), n, max(hold_days), sum(hold_days)/n, min(hold_days), max(volume), sum(volume)/n, min(volume), max(profit), sum(profit)/n, min(profit))

# last = [10, None, None, None, 500]
# A = [[0, "Buy", 20, 200, 100], [1, "Sell", 10, 100, 200], [2, "Buy", 10, 100, 300], [3, "Sell", 19, 200, 250]]
# print(history2profit_segment(A, last))

# A = [[pd.Timestamp('2021-05-16 00:00:00'), 'Buy', 0.086896, 50.0, 575.4],
# [pd.Timestamp('2021-05-17 00:00:00'), 'Sell', 0.017582, 10.0, 568.76],
# [pd.Timestamp('2021-05-18 00:00:00'), 'Buy', 0.254948, 150.0, 588.36],
# [pd.Timestamp('2021-05-20 00:00:00'), 'Buy', 0.016735, 9.75, 582.61],
# [pd.Timestamp('2021-06-29 00:00:00'), 'Buy', 7.023947, 4768.5, 678.89],
# [pd.Timestamp('2021-07-29 00:00:00'), 'Sell', 7.0, 4713.0, 673.29],
# [pd.Timestamp('2021-07-29 00:00:00'), 'Sell', 0.364944, 245.91, 673.83],
# [pd.Timestamp('2021-09-23 00:00:00'), 'Buy', 4.0, 3014.38, 753.6],
# [pd.Timestamp('2021-10-13 00:00:00'), 'Sell', 4.0, 3234.2, 808.55],
# [pd.Timestamp('2021-11-02 00:00:00'), 'Buy', 2.0, 2359.2, 1179.6],
# [pd.Timestamp('2021-11-02 00:00:00'), 'Buy', 3.0, 3540.65, 1180.22],
# [pd.Timestamp('2021-11-02 00:00:00'), 'Sell', 5.0, 5810.0, 1162.0],
# [pd.Timestamp('2021-11-05 00:00:00'), 'Buy', 4.0, 4929.32, 1232.33],
# [pd.Timestamp('2021-11-08 00:00:00'), 'Sell', 4.0, 4757.84, 1189.46],
# [pd.Timestamp('2021-11-23 00:00:00'), 'Buy', 9.0, 9990.0, 1110.0],
# [pd.Timestamp('2021-12-02 00:00:00'), 'Sell', 9.0, 9891.0, 1099.0],
# [pd.Timestamp('2021-12-09 00:00:00'), 'Buy', 10.0, 10000.0, 1000.0],
# [pd.Timestamp('2021-12-16 00:00:00'), 'Sell', 10.0, 9350.0, 935.0],
# [pd.Timestamp('2021-12-23 00:00:00'), 'Buy', 22.0, 23478.4, 1067.2],
# [pd.Timestamp('2021-12-27 00:00:00'), 'Sell', 22.0, 24024.0, 1092.0],
# [pd.Timestamp('2021-12-27 00:00:00'), 'Buy', 18.0, 19758.06, 1097.67],
# [pd.Timestamp('2021-12-28 00:00:00'), 'Sell', 18.0, 19773.0, 1098.5]]
#
# last = None
# print(history2profit_segment(A, last))
