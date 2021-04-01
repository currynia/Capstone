import json

class reader:
    
    def __init__(self):
        self.stops = []
    
    def stops_reader(self,file):
        """
        Reads in json file containing bus stop data and append it into an array

        Args:
            file (json): json file containing bus stop data

        Returns:
            list: array with all the bus stop data
        """        
        with open(file,'r') as f:
            data = json.load(f)
            for stops in data:
                self.stops.append(stops)
        return self.stops

    
