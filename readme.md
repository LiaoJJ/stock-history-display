# Stock History Display

Available on Heroku: https://stock-history-display.herokuapp.com/

## Introduction
The purpose of this project is something an easy yearly review tool for your stock performance. This app will help you get a very quick and clear view of your past invesment, about whether you earn or loss, about how much you earn and loss, about when you buy-in and sell-out, about the volume in related buy/sell threade. We both know it's pretty annoying to review your Robinhood history long list and it's not clear at all.

By the help of this app, users will be able to have a better view from their past investment, and also get some feedback from it. This is super important in improving future stock market performance. 

## Sample result
![](static/TSLA_1y_result.png)
```
Metrics:
- total profit: -239.29836702000216
- total thread transactions: 14
- hold days: max=74, avg=22.928571428571427, min=0
- volume: max=22.0, avg=5.670180428571428, min=0.016735
- profit: max=545.599999999999, avg=-17.092740501428725, min=-650.0

profit_segment_list:
[start_time, start_unit_price, end_time, end_unit_price, volume, profit]
2021-05-16, 575.40, 2021-05-17, 568.76, 0.02, -0.12
2021-05-16, 575.40, 2021-07-29, 673.29, 0.07, 6.79
2021-05-18, 588.36, 2021-07-29, 673.29, 0.25, 21.65
2021-05-20, 582.61, 2021-07-29, 673.29, 0.02, 1.52
2021-06-29, 678.89, 2021-07-29, 673.29, 6.66, -37.29
2021-06-29, 678.89, 2021-07-29, 673.83, 0.36, -1.85
2021-09-23, 753.60, 2021-10-13, 808.55, 4.00, 219.80
2021-11-02, 1179.60, 2021-11-02, 1162.00, 2.00, -35.20
2021-11-02, 1180.22, 2021-11-02, 1162.00, 3.00, -54.66
2021-11-05, 1232.33, 2021-11-08, 1189.46, 4.00, -171.48
2021-11-23, 1110.00, 2021-12-02, 1099.00, 9.00, -99.00
2021-12-09, 1000.00, 2021-12-16, 935.00, 10.00, -650.00
2021-12-23, 1067.20, 2021-12-27, 1092.00, 22.00, 545.60
2021-12-27, 1097.67, 2021-12-28, 1098.50, 18.00, 14.94
```

## System Structure
![](static/sd2.png)

## Steps
- Step 1: Input stock abbreviation: By default, it is TSLA, which is the abbreviation of TESLA
- Step 2: Copy and paste buy/sell histories from [Robinhood history page](https://robinhood.com/history/e39ed23a-7bd1-4587-b060-71988d9ef483), make sure you follow the format, more detail on [How to Copy History](#How-to-Copy-History)
- Step 3: (Optional) Choose a period: 1 year or 5 year. Also, you can choose a filter which could filter out small profit line to reduce distraction, default = 10.
- Step 4: Click submit, then you should see buy/sell history picture attached to your stock line chart as below

## Current Feature
- Tech Stacks: `Python, Flask, Html, JSON, Docker, Heroku`
- fetch Stock data from Yahoo Finance API
- persist Stock data as file to reduce duplicated Yahoo Finance API request 
- parse history data: the personal operations history, like when you make a buy-in or sell-out transaction, this will add a datapoint into history. This app support parse data from history following Robinhood history page format. You may paste history from Robinhood history page.
- [Thread transaction](#Thread-Transaction) generated from history data
- bypass browser cache by random number naming
- support parsing complicated transactions and generating simple buy or sell threads. 
- clear green and red view for earn and loss. 4K (3840x2160) definition picture for 1 year data. Extended X-size when period is long. 
- support split in history
- Display statistics regarding thread transaction. 

## Thread Transaction
This is also called profit_segment in the code, which is a segment of information regarding a thread of investment. I will explain this with a example
Let's say somebody make below transactions:

```
Buy 2 stocks at day 0, with unit price 1
Sell 1 stocks at day 1, with unit price 2
Buy 1 stocks at day 2, with unit price 3
Sell 2 stocks at day 3, with unit price 2
```
Then, this will generate below thread transactions:
```
[start_time, end_time, volume, profit]
[day 0, day 1, 1, 1]
[day 0, day 3, 1, 1]
[day 2, day 3, 1, -1]
```

## Future
- Redis Cache
  - for merged picture, key is `stock name + period + interval + SHA256(history data)`
  - for stock data, key is `stock name + period + interval`
  - for history data, key is `SHA256(history data)`
- MySQL storage
  - 3 tables: stock data table, history data table and users table
- support personal accounts, and support google login in
- better de-deplicate mechanism, potentially using hash, SHA256
- scale by different time length, year, month, day, etc
- a broader system design
- beautify UI by Bootstrap

## How to Copy History
![](static/his.png)

## Reference
- https://github.com/ranaroussi/yfinance
- https://robinhood.com
- https://heroku.com/
- and many others
