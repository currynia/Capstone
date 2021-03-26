import sqlite3


commands = {'bus_stops':
'''
CREATE TABLE IF NOT EXISTS stops(
    "BusStopCode" TEXT UNIQUE PRIMARY KEY,
    "RoadName" TEXT,
    "Description" TEXT,
    "Latitude" REAL
    "Longitude" REAL
''',
'bus_insert':
'''
INSERT INTO stops VALUES(?,?,?,?,?);
'''
}

class dataStore:
    def connect(self):
        conn = sqlite3.connect('bus')
        
    
    def createtable(self):
        conn = sqlite3.connect('bus')
        cur = conn.cursor()
        cur.execute(commands.get('bus_stops'))
        cur.commit()
    
    def insert(self,data):
        for stop in data:
            cur.execute('bus_insert',(stop['BusStopCode'],stop['RoadName'],stop['Description'],stop['Latitude'],stop['Longitude'],))
            cur.commit()

        