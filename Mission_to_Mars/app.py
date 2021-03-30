from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo 
import scrape_mars


app = Flask(__name__)

mongo = PyMongo(app)

#--! Create New HTML Template#

@app.route("/")
def index():
    mars = mongdo.db.mars.find_one()
    return render_template("index.html",mars=mars)


@app.route("/scape")
def index():
    mars = mongo.db.mars
    mars_data = scarpe_mars.scrape()
    mars.update(
        {},
        mars_data,
        upsert=True
    )
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)