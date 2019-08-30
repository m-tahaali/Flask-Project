import sqlalchemy
from flask import Flask, render_template, request
import markupsafe
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///localhost/db'
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


@app.route("/post", methods=['POST', 'GET', ''])
def posthtml():
    if request.method == 'GET':
        if request.args.get('id'):
            postid = request.args.get('id')
            post = {'title': '', 'author': '', 'date': '', 'heading': '', 'subheading': '',
                    'content': markupsafe.Markup('')}
        else:
            post = {'title': '', 'author': '', 'date': '', 'heading': 'No Post ID Found', 'subheading': '',
                    'content': markupsafe.Markup('')}
    return render_template("post.html", post=post)


app.run(debug=True, port=80, host="0.0.0.0")
