import json

class reader:
    def __init__(self):
        self.stops = []
    
    def stops_reader(self,file):
        with open(file,'r') as f:
            data = json.load(f)
            for stops in data:
                self.stops.append(stops)
        return self.stops

    
