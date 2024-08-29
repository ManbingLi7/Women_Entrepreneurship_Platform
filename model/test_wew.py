from flask import Flask
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


# Defining the home page of our site
@app.route("/")
def home():
    return render_template("index.html", content='Testing')


if __name__ == "__main__":
    app.run()



