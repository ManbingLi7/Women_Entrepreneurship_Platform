from flask import Flask
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


# Defining the home page of our site
@app.route("/<name>")
def home(name):
    return render_template("index.html")

'''
@app.route("/<name>")
def user(name):
        return f"Hallo {name}!"

@app.route("/admin")
def admin():
	return redirect(url_for("home"))
'''

if __name__ == "__main__":
    app.run()



