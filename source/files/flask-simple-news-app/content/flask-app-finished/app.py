from filter import get_birthday_rows_by_month_day
from htmlmaker import birthday_html
from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def homepage():
    the_date = datetime.now()
    the_mthday = the_date.strftime('%m-%d')
    data_rows = get_birthday_rows_by_month_day(the_mthday)
    return birthday_html(data_rows, the_date)

@app.route('/onthisdate/<yyyymmdd>')
def on_this_date(yyyymmdd):
    the_date = datetime.strptime(yyyymmdd, '%Y-%m-%d')
    the_mthday = the_date.strftime('%m-%d')
    data_rows = get_birthday_rows_by_month_day(the_mthday)
    return birthday_html(data_rows, the_date)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
