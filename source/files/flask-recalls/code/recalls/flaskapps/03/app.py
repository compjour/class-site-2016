from flask import Flask
from flask import render_template
from datetime import datetime
from datafoo import get_data
recalls_data = get_data()


app = Flask(__name__)


@app.route("/")
def homepage():
    tname = 'index.html'
    return render_template(tname,
                recalls_count=len(recalls_data),
                recalls_list = recalls_data)

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
