from rosaline import rosaline
from datastore import dataStore
from dataread import reader
from flask import Flask,request,render_template
from sort_algo import sortalgo

sortalgo = sortalgo()
rosaline = rosaline()
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

@app.route('/nearest', methods=['POST','GET'])
def nearest():
    # try:
    location = request.form['id']
    location = location.split(',')
    location = {'lat':float(location[0]),'long':float(location[1])}
    submission_successful = True
    stops_coord = datastore.get_records('bus.db','get_coord')
    distance_data = []
    for coords in stops_coord:
        distance_data.append({'BusstopCode':coords[0],'distance':rosaline.haversine(location['lat'],location['long'],coords[1],coords[2])})
    distance_data = sortalgo.sort_distance(distance_data)
    nearest = datastore.get_records('bus.db','code_to_name',(distance_data[0]['BusstopCode'],))
    nearest_busstop = nearest[0][0]
    return render_template('nearest.html',submission_successful=submission_successful,nearest_busstop = nearest_busstop)

    # except:
    return render_template('nearest.html')





app.run(debug=True)