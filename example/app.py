from flask import Flask, render_template
from flask_collections import Collections


app = Flask(__name__)
app.config["COLLECTIONS"] = {"posts": {"layout": "post.html"}}
Collections(app)


@app.route("/")
def index():
    return render_template("index.html")
