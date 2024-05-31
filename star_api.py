from flask import Flask
import pandas as pd
from data import data

app = Flask(__name__)

@app.route("/")
def display_data():
    return data

@app.route("/<name>")
def display_star_data(name):
    for i in range(len(data)):
        if data[i]['Name'] == name:
            return data[i]
        else:
            return "Star data was not found"

if __name__ == '__main__':
    app.run()