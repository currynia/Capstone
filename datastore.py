import sqlite3


commands = {'bus_stops':
'''
CREATE TABLE IF NOT EXISTS stops(
    "BusStopCode" TEXT UNIQUE PRIMARY KEY,
    "RoadName" TEXT,
    "Description" TEXT,
    "Latitude" REAL,
    "Longitude" REAL);
''',
'bus_insert':
'''
INSERT INTO stops VALUES(?,?,?,?,?);
'''
}

class dataStore:
    def createdb(self,db):
        db = sqlite3.connect(db)
    
    def createtable(self,db):
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(commands.get('bus_stops'))
        conn.commit()
    
    def insert(self,data,db):
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        for stop in data:
            cur.execute(commands.get('bus_insert'),(stop['BusStopCode'],stop['RoadName'],stop['Description'],stop['Latitude'],stop['Longitude'],))
            conn.commit()

        