#import dependencies
from flask import Flask, render_template, redirect, url_for


#set up flask
app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index2.html')

@app.route('/results')
def results():
    return render_template('results.html')

@app.route('/data')
def data(state: dict) -> dict:
    info = mongo.db.Sec8_county_merged

    info.find({state})
    
    return render_template('table.html', info=info)

if __name__ == "__main__":
    app.run(debug=True, port=8001)











