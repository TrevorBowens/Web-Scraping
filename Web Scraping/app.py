# import necessary libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape

# create instance of Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/stories"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/weather_app")


# create route that renders index.html template and finds documents from mongo
@app.route("/")
def home():

    # Find data
    stories = mongo.db.collection.find()
    mars = scrape.mars_table()
    images=scrape.
    # return template and data
    return render_template("Mars.html", stories=stories, mars=mars)


# Route that will trigger scrape functions
@app.route("/scrape")
def scrape2():

    # Run scraped functions
    article, mars_weather = scrape.scrape_article()
    #mars_weather = scrape_mars_weather()

    # Store results into a dictionary
    News = {
        "news_title": article["title"],
        "paragraphs": article["paragraphs"],
        "temperatures": mars_weather,
        
    }

    # Insert forecast into database
    mongo.db.collection.insert_one(News)

    # Redirect back to home page
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
