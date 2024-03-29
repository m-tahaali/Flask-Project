from datetime import datetime

from flask import Flask, render_template, request, flash
import markupsafe
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect
from flask_login import UserMixin
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'rjrJWXVQashrOA/s58ODMQ=='
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://HAAcmJ5HTU:oRnOUJQsOK@remotemysql.com:3306/HAAcmJ5HTU'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Posts(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    pub_date = db.Column(db.DateTime(), nullable=False,
                         default=datetime.utcnow())
    author = db.Column(db.String(80), nullable=False)
    heading = db.Column(db.Text, nullable=False)
    subheading = db.Column(db.Text, nullable=False)
    image = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Post %r>' % self.title


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000), unique=True)
    rank = db.Column(db.String(1000))


db.create_all()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))


@app.route("/")
def home():
    posts = Posts.query.order_by(Posts.pub_date)
    post1 = {'heading': '', 'subheading': '',
             'author': '', 'date': '', 'show': '', 'postid': ''}
    post2 = {'heading': '', 'subheading': '',
             'author': '', 'date': '', 'show': '', 'postid': ''}
    post3 = {'heading': '', 'subheading': '',
             'author': '', 'date': '', 'show': '', 'postid': ''}
    post4 = {'heading': '', 'subheading': '',
             'author': '', 'date': '', 'show': '', 'postid': ''}
    if posts.get(1):
        post = posts.get(1)
        post1 = {
            'heading': post.heading,
            'subheading': post.subheading,
            'author': post.author,
            'date': post.pub_date,
            'show': 'true',
            'postid': str(post.id)
        }
    if posts.get(2):
        post = posts.get(2)
        post2 = {
            'heading': post.heading,
            'subheading': post.subheading,
            'author': post.author,
            'date': post.pub_date,
            'show': 'true',
            'postid': str(post.id)
        }
    if posts.get(3):
        post = posts.get(3)
        post3 = {
            'heading': post.heading,
            'subheading': post.subheading,
            'author': post.author,
            'date': post.pub_date,
            'show': 'true',
            'postid': str(post.id)
        }
    if posts.get(4):
        post = posts.get(4)
        post4 = {
            'heading': post.heading,
            'subheading': post.subheading,
            'author': post.author,
            'date': post.pub_date,
            'show': 'true',
            'postid': str(post.id)
        }
    return render_template("index.html", post1=post1, post2=post2, post3=post3, post4=post4)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/post/<postid>", methods=['POST', 'GET'])
def posthtml(postid):
    if request.method == 'GET':
        if Posts.query.filter_by(id=postid).first():
            selected = Posts.query.filter_by(id=postid).first()
            post = {'title': selected.title,
                    'author': selected.author,
                    'date': selected.pub_date,
                    'heading': selected.heading,
                    'subheading': selected.subheading,
                    'content': markupsafe.Markup(selected.content),
                    'image': selected.image}
        else:
            post = {'title': '', 'author': '', 'date': '', 'heading': 'No Post ID Found', 'subheading': '',
                    'content': markupsafe.Markup(''), 'image': ''}
    return render_template("post.html", post=post)


@app.route("/add", methods=['POST', 'GET'])
def addpost():
    if request.method == 'POST':
        post = Posts(title=request.form.get('title'),
                     content=request.form.get('content'),
                     heading=request.form.get('heading'),
                     subheading=request.form.get('subheading'),
                     author=request.form.get('author'),
                     image=request.form.get('image'))
        db.session.add(post)
        db.session.commit()
        post = {'title': 'Success', 'author': '', 'date': '', 'heading': 'Succes Your Post Id is ' + str(post.id),
                'subheading': '',
                'content': markupsafe.Markup('<a href="/post/' + str(post.id) + '"> Go To: <br><h3>' + post.heading
                                             + '</h3> <h4>' + post.subheading + '</h4></a>'),
                'image': ''}
        return render_template("post.html", post=post)
    else:
        return render_template("addpost.html")


@app.route("/signup", methods=['POST','GET'])
def signup_post():
    if request.method=="POST":
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')

        useremail = User.query.filter_by(email=email).first()
        username = User.query.filter_by(name=name).first()

        if useremail:
            flash('Email address already exists')
            return redirect('/signup')
        if username:
            flash(' already exists')
            return redirect('/signup')

        # if the above check passes, then we know the user has the right credentials

        new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'), rank='guest')
        db.session.add(new_user)
        db.session.commit()

        return redirect("/login")
    else:
        return render_template('signup.html')



@app.route('/login', methods=['POST', 'GET'])
def login_post():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        user = User.query.filter_by(email=email).first()

        # check if user actually exists
        # take the user supplied password, hash it, and compare it to the hashed password in database
        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            # if user doesn't exist or password is wrong, reload the page
            return redirect("/login")

        # if the above check passes, then we know the user has the right credentials
        login_user(user, remember=remember)
        return redirect("/")
    else:
        return render_template("login.html")


app.run(debug=True, port=80, host="0.0.0.0")
