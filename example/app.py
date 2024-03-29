from flask import Flask, render_template, request
from flask_collections import Collections


app = Flask(__name__)
app.config["COLLECTIONS"] = {
    "posts": {
        "layout": "post.html"
    }
}
Collections(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/category", methods=["POST"])
def create_category(self):
    name = request.form["name"]
    slug = name.lower().replace(" ", "-")
    app.collections["categories"].save(slug, {"name": name})