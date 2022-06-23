from flask import Flask, render_template, redirect
from flask import url_for, request, flash
from flask_pymongo import PyMongo
import scrape_mars
# Creating an instance for Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
#app.config["MONGO_URI"] = "mongodb://localhost:27017/phone_app"
#mongo = PyMongo(app)

# Or set inline
mongo = PyMongo(app, uri="mongodb://localhost:27017/phone_app")


@app.route("/scrape")
def scraper():
    marsdict = mongo.db.marsdict
    marsdict_data = scrape_mars.scrape()
    #marsdict.insert_one(marsdict_data)
    marsdict.update({}, marsdict_data, upsert=True)
    return redirect("/", code=302)

@app.route("/")
def index():
    marsdict = mongo.db.marsdict.find_one()
    return render_template("index.html", marsdict=marsdict)





if __name__ == "__main__":
    app.run(debug=True)
