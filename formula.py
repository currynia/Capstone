from math import radians, cos, sin, asin, sqrt


class Formula:
    def haversine(self,lat1,long1,lat2,long2):
        """
        Calculates the distance between 2 points

        Args:
            lat1 (float): latitude of coordinate 1
            long1 (float): longitude of coordinate 1
            lat2 (float): latitude of coordinate 2
            long2 (float): longtiude of coordinate 2
        
        Returns:
            float: distance between coordinate 1 and coordinate 2
        
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
    
    