from flask import Flask
from flask import render_template
from datetime import datetime
from datafoo import get_data
recalls_data = get_data()


app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template('index.html',
                recalls_count=len(recalls_data),
                recalls_list = recalls_data)

@app.route("/product_type/<product_id>")
def product_type(product_id):
    pdata = []
    for row in recalls_data:
        if row['product_id'] == product_id:
            pdata.append(row)
    return render_template('product_type.html',
                product_id=product_id,
                recalls_count=len(pdata),
                recalls_list = pdata)

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
