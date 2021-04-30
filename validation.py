class Validation:
    def __init__(self,lat,long):
        self.lat = lat
        self.long = long

    def dot_counter(self):
        """
        Counts the number of '.' in a latitude and longitude respectively
        Returns:
            list: [number of dots in latitude, number of dots in longitude]
        """        
        return [self.lat.count('.'),self.long.count('.')]

class Check(Validation):
    def checker(self):
        """
        Check function that validates if the latitiude and longtiude are in the correct format

        Returns:
            boolean: Returns True if the coordinates are in the correct format. Else, returns False
        """        
        dot_count = self.dot_counter()
        print(dot_count)
        if dot_count[0] < 2 and dot_count[1] < 2:
            self.lat,self.long = self.lat.replace('.',''),self.long.replace('.','')
            if self.lat.isdigit() and self.long.isdigit():
                return True
            else:
                return False
        else:
            return False

        

