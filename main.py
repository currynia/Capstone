import sqlite3
from datastore import dataStore
from dataread import reader
from flask import Flask,request,rende_template

datastore = dataStore()
datastore.connect()
reader = reader()
data = reader.stops_reader('bus_stops.json')

app = Flask(__name__)

@app.route('/')
def root():
    return render_template()