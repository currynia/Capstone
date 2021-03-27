from math import radians, cos, sin, asin, sqrt


class rosaline:
    def haversine(lat1,long1,lat2,long2):
        """
        Calculates the distance between 2 points
        
        """
        #convert to radians
        lat1,long1,lat2,long2 = map(radians, (lon1,lat1,lon2,lat2))

        #haversine formula
        delta_lon = lon2 - lon1
        delta_lat = lat2 - lat1
         a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a)) 
        r = 6371 # Radius of earth in kilometers. Use 3956 for miles
        return c * r