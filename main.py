from formula import formula
from datastore import dataStore
from dataread import reader
from flask import Flask,request,render_template
from sort_algo import sortalgo

sortalgo = sortalgo()
formula = formula()
datastore = dataStore()
datastore.createdb('bus.db')
datastore.createtable('bus.db','bus_stops')
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

@app.route('/nearestbusstop', methods=['POST','GET'])
def nearest():
    try:
        lat = request.form['Lat']
        long = request.form['Long']
        location = {'lat':float(lat),'long':float(long)}
        submission_successful = True
        stops = datastore.get_records('bus.db','get_coord')
        distance_data = []
        for stop in stops:
            distance_data.append({'BusstopCode':stop[0],'Description':stop[1],'distance':formula.haversine(location['lat'],location['long'],stop[2],stop[3])})
        distance_data = sortalgo.sort_distance(distance_data)
        for distance in distance_data:
            distance.update({'distance':round(distance['distance'],2)})
    
        return render_template('nearest.html',submission_successful=submission_successful,distance_data = distance_data)
    
    except:
        return render_template('nearest.html')





app.run('0.0.0.0',debug=True)