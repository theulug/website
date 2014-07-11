from flask import Flask, render_template, request, redirect, url_for

ulug = Flask(__name__)
here = ulug.root_path

@ulug.route("/")
def index():
    return render_template("home.html")

@ulug.route("/irc")
def irc():
    return render_template("irc.html")

@ulug.route("/constitution")
def constitution():
    return render_template("constitution.html")

@ulug.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    ulug.run(debug=True)
