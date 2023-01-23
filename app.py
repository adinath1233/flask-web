#First web application in flask

from flask import Flask, render_template

app = Flask(__name__)

#Running html file from route
#Create folder 'templates' and create html file in it
@app.route("/")
def first_route():
    return render_template("home.html")

@app.route("/about")
def about_page():
    return "<h1>This is About page</h1>"

@app.route("/contact")
def contact_page():
    return "<h1>This is Contact page</h1>"

@app.route("/slr")
def slr():
    return render_template("slr.html")

app.run(debug=True)