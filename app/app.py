# Step 2 continued - MongoDB and Flask Application
# Create a root route / that will query your Mongo database and pass the mars data into an 
# HTML template to display the data

# Import dependencies
import pymongo as PyMongo
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scrape_mars

# Flask setup
app = Flask(__name__)

# Databased setup: use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Set up root route to query MongoDB
@app.route("/")
def index():
    # Pass mars data into HTML template to display the data
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

# Set up scrape route to import scrape_mars script
@app.route("/scrape")
def scrape():
    # Call scrape function
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape_all()
    # Store return value in Mongo as Python dictionary
    mars.replace_one({}, mars_data, upsert=True)
    return "Scraping successful!"

if __name__ == "__main__":
    app.run()