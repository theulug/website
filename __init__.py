from flask import Flask, render_template, request, redirect, url_for

ulug = Flask(__name__)
here = ulug.root_path

@ulug.route("/")
def index():
    return "The ULUG website!"

@ulug.route("/docs")
def docs():
    return "Here for documentation"

if __name__ == "__main__":
    ulug.run()
