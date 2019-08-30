from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import markupsafe
import datetime

class post_props():
    def __init__(self,title="Post",author="Ali or Taha",date=datetime.datetime.now().strftime("%x"),heading="Ali",subheading=None,content=None):
        self.title=title
        self.author=author
        self.date=date
        self.heading=heading
        self.subheading=subheading
        self.content=content

a=post_props(heading="Taha")

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/post")
def post():
    return render_template("post.html", post=a)


app.run(debug=True, port=80, host="0.0.0.0")