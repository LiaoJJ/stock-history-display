from flask import Flask, render_template, request
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname("./src"))
sys.path.append(os.path.dirname("./data"))
sys.path.append(os.path.dirname("./static"))
from src.history_data_processor import get_default_history_data, process_history
from src.controller import process
import random
import matplotlib


default_stock_abbr = "TSLA"
default_histories = get_default_history_data(default_stock_abbr)
default_filter=10
period_list=("1y", "5y")

matplotlib.use('Agg')
app = Flask(__name__)


# @app.route('/', methods =["GET"])
# def get_index():
#     return render_template("index.html", user_image = "static/TSLA_1y_result.png", abbr = default_stock_abbr, histories=default_histories, period_list = period_list, selected_period = period_list[0], filter=default_filter)

@app.route('/', methods = ["POST", "GET"])
def post_index():
    stock_abbr = request.form.get("Stock Abbreviation") or default_stock_abbr
    histories = request.form.get("Buy-in Sell-out Histories of Robinhood") or default_histories
    period = request.form.get("period") or period_list[0]
    filter=int(request.form.get("filter") or default_filter)
    rand = str(random.random()) # prevent brower cache and make sure users get updated picture
    error_message, result_text = "", ""
    try:
        result_text = process(histories, stock_abbr, period, filter, rand)
    except Exception as e:
        error_message = e
        print(e)
    picture_path = "static/{}_{}_result_{}.png".format(stock_abbr, period, rand)
    resp = render_template("index.html", user_image=picture_path, abbr=stock_abbr, histories=histories,
                           period_list=period_list, selected_period=period, filter=filter, error_message=error_message, result_text = result_text)
    return resp


port = int(os.environ.get('PORT', 8000))
if __name__ == '__main__':
	app.run(host='0.0.0.0',port=port)
