from math import radians, cos, sin, asin, sqrt


class rosaline:
    def haversine(self,lat1,long1,lat2,long2):
        """
        Calculates the distance between 2 points
        
        """
        #convert to radians
        lat1,long1,lat2,long2 = map(radians, (lat1,long1,lat2,long2))

        #haversine formula
        delta_long = long2 - long1
        delta_lat = lat2 - lat1
        a = sin(delta_lat/2)**2 + cos(lat1) * cos(lat2) * sin(delta_long/2)**2
        c = 2 * asin(sqrt(a)) 
        r = 6371 # Radius of earth in kilometers. Use 3956 for miles
        return c * r
    
    