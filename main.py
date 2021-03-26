import sqlite3
from datastore import dataStore
from dataread import reader
from flask import Flask,request,render_template

datastore = dataStore()
datastore.createdb('bus.db')
datastore.createtable('bus.db')
reader = reader()
data = reader.stops_reader('bus_stops.json')

try:
    #Store data only for the first time
    datastore.insert(data,'bus.db')
except:
    pass

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/nearest', methods=['POST','GET'])
def nearest():
    return render_template('nearest.html')

@app.route('/nearest1', methods=['POST','GET'])
def nearest1():
    print(request.form['id'])
    return ('''asdasd''')



app.run(debug=True)