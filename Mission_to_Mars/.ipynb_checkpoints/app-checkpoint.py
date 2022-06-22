from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
# Creating an instance for Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
#app.config["MONGO_URI"] = "mongodb://localhost:27017/phone_app"
#mongo = PyMongo(app)

# Or set inline
mongo = PyMongo(app, uri="mongodb://localhost:27017/phone_app")


@app.route("/")
def index():
    marsdict = mongo.db.listings.find_one()
    return render_template("index.html", marsdict=marsdict)


@app.route("/scrape")
def scraper():
    marsdict = mongo.db.listings
    marsdict_data = scrape_mars.scrape()
    marsdict.insert_one(marsdict_data)
    #listings.update({}, listings_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)