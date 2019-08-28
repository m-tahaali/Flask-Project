from flask import Flask, render_template
import sqlalchemy

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


app.run(debug=True,port=80,host="0.0.0.0")
