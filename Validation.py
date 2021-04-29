class Validation:
    def __init__(self,lat,long):
        self.lat = lat
        self.long = long

    def dot_counter(self):
        return [self.lat.count('.'),self.long.count('.')]

         

class Check(Validation):
    def checker(self):
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

        

