import json

class reader:
    
    def __init__(self):
        self.stops = []
    
    def stops_reader(self,file):
        '''
        Takes in a json file containing the data of the bus stops and returns a list containing the data
        '''
        with open(file,'r') as f:
            data = json.load(f)
            for stops in data:
                self.stops.append(stops)
        return self.stops

    
