# Stock History Display

Available on Heroku: https://stock-history-display.herokuapp.com/

## The purpose
The purpose of this project is something like a easy yearly review for your stock performance. This app will help you get a very quick and clear view of your past invesment, about whether you earn or loss, about how much you earn and loss, about when you buy-in and sell-out, about the volume in related buy/sell threade. We both know it's pretty annoying to review your Robinhood history long list and it's not clear at all.

By the help of this app, users will be able to have a better view from their past investment, and also get some feedback from it. This is super important in improving future stock market performance. 

## Sample result
![](static/TSLA_1y_result.png)

## Steps
- Step 1: Input stock abbreviation: By default, it is TSLA, which is the abbreviation of TESLA

- Step 2: Copy and paste buy/sell histories from [Robinhood history page](https://robinhood.com/history/e39ed23a-7bd1-4587-b060-71988d9ef483), make sure you follow the format, 

- Step 3: (Optional) Choose a period: 1 year or 5 year. Also, you can choose a filter which could filter out small profit line to reduce distraction, default = 10.

- Step 4: Click submit, then you should see buy/sell history picture attached to your stock line chart as below

## Current Feature
- An interactive web app based on Flask, Python, html
- Deployed on Heroku using Docker
- fetch Stock data from Yahoo Finance API
- history: the personal operations history, like when you make a buy-in or sell-out transaction, this will add a datapoint into history. This app support parse data from history following Robinhood history page format. You may paste history from Robinhood history page.
- bypass browser cache by random number naming
- support parsing complicated transactions and generating threads. 
- clear green and red view for earn and loss. very high definition picture.


## Future
- Cache
- MySQL storage
- support personal accounts, and support google login in
- better de-deplicate mechanism
- scale by different time length, year, month, day, etc



## Reference
- https://github.com/ranaroussi/yfinance
- https://robinhood.com
- https://heroku.com/
- and many others
