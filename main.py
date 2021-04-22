from formula import Formula
from datastore import DataStore
from dataread import Reader
from sort_algo import SortAlgo
from flask import Flask,request,render_template

#initialise objects
sortalgo = SortAlgo()
formula = Formula()
datastore = DataStore()
reader = Reader()

datastore.createdb('bus.db') #create database
datastore.createtable('bus.db','bus_stops') #create table
data = reader.stops_reader('bus_stops.json') #convert bus  data to list
datastore.coord_insert(data,'bus.db') #insert bus stop data into database

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/nearestbusstop', methods=['GET'])
def nearest():
    try:
        lat = request.args['Lat']
        long = request.args['Long']
        submission_successful = True
    except:
        submission_successful = False
    
    if submission_successful:
        #get latitude and longitude from form and stores it into a dictionary
        lat_check = 'None'
        long_check = 'None'
        if lat.count('.') == 1 and long.count('.') == 1:
            lat_check,long_check = lat.replace('.',''),long.replace('.','')
        if lat_check.isdigit() and long_check.isdigit(): 
            location = {'lat':float(lat),'long':float(long)}
            submission_successful = True
            stops = datastore.get_records('bus.db','get_coord')
            distance_data = [] 
            for stop in stops: #calculate distance of each bus stop from coordinates
                distance_data.append({'BusstopCode':stop[0],'Description':stop[1],'distance':formula.haversine(location['lat'],location['long'],stop[2],stop[3])})
            distance_data = sortalgo.sort_distance(distance_data) #sort array based on distance from specified coordinates
            for distance in distance_data: #convert distance values into 2dp
                distance.update({'distance':round(distance['distance'],2)})
            return render_template('nearest.html',submission_successful=submission_successful,distance_data = distance_data)
    
        else:
            error = "Please input numbers only"
            return render_template('nearest.html',error=error)
    else:
        return render_template('nearest.html')

@app.route('/help')
def help():
    return render_template('help.html')

app.run('0.0.0.0')