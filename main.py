from datetime import datetime

from flask import Flask, render_template, request
import markupsafe
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://HAAcmJ5HTU:oRnOUJQsOK@remotemysql.com:3306/HAAcmJ5HTU'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False,
                         default=datetime.utcnow)
    author = db.Column(db.String(80), nullable=False)
    heading = db.Column(db.Text, nullable=False)
    subheading = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Post %r>' % self.title


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
        if request.args.get('id') and Posts.query.filter_by(id=request.args.get('id')).first():
            postid = request.args.get('id')
            selected = Posts.query.filter_by(id=postid).first()
            post = {'title': selected.title,
                    'author': selected.author,
                    'date': selected.pub_date,
                    'heading': selected.heading,
                    'subheading': selected.subheading,
                    'content': selected.content}
        else:
            post = {'title': '', 'author': '', 'date': '', 'heading': 'No Post ID Found', 'subheading': '',
                    'content': markupsafe.Markup('')}
    return render_template("post.html", post=post)


app.run(debug=True, port=80, host="0.0.0.0")