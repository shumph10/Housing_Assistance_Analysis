#import dependencies
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping
from static.config import MONGO_URL

#set up flask
app = Flask(__name__)

#Use pyMondo to set up mongo connection
app.config["MONGO_URL"] = MONGO_URL
mongo = PyMongo(app)












