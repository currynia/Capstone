import json

class Reader:
    
    def __init__(self):
        self.stops = [] #Array to store bus stop data
    
    def stops_reader(self,file):
        """
        Reads in json file containing bus stop data and append it into an array

        Args:
            file (json): json file containing bus stop data

        Returns:
            list: array with all the bus stop data in the format [BusStopcode,Description,Latitude,Longitude]
        """        
        with open(file,'r') as f:
            data = json.load(f)
            for stops in data:
                self.stops.append(stops)
        
    
