from flask import Flask
from datafoo import get_data

app = Flask(__name__)
datarows = get_data()

@app.route("/")
def homepage():
    htmlstr = "<h1>Hello world!</h1>"
    htmlstr += "<p>There have been {num} recalls</p>".format(num=len(datarows))
    for d in datarows:
        htmlstr += """<p><a href="{url}">{title}</a></p>""".format(title=d['Title'], url=d['URL'])
    return htmlstr

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
