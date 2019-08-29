from flask import Flask, render_template
import markupsafe
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://test'
db = SQLAlchemy(app)


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
def posthtml():
    post = {'title': '', 'author': '', 'date': '', 'heading': '', 'subheading': '',
            'content': markupsafe.Markup('')}
    return render_template("post.html", post=post)


app.run(debug=True, port=80, host="0.0.0.0")
