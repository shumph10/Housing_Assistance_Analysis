#import dependencies
from flask import Flask, render_template, redirect, url_for
# from flask_pymongo import PyMongo
# import scraping
# import random
# import requests
# from config import MONGO_URL


#set up flask
app = Flask(__name__)

#Use pyMondo to set up mongo connection
# app.config["MONGO_URL"] = MONGO_URL
# mongo = PyMongo(app)


@app.route('/')
def home():
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True, port=5001)











