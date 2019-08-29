from flask import Flask, render_template
import sqlalchemy
import markupsafe

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/post")
def posts():
    return render_template("post.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post")
def post():
    post = {'title': '', 'author': '', 'date': '', 'heading': '', 'subheading': '',
            'content': markupsafe.Markup('<h1> Test </h1>')}
    return render_template("post.html", post=post)


app.run(debug=True, port=80, host="0.0.0.0")
