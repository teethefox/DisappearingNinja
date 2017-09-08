from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ninja")
def process():
    return render_template("ninja.html")
@app.route("/blue")
def blue():
    return render_template("blue.html")
@app.route('/red')
def red():
    return render_template("red.html")
@app.route("/orange")
def orange():
    return render_template("orange.html")
@app.route("/purple")
def purple():
    return render_template("purple.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('notapril.html'), 404
app.run(debug=True)