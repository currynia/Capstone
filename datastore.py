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
''',

'get_coord':
'''
SELECT "BusStopCode","Description", "Latitude","Longitude"
FROM "stops" 
''',

'code_to_name':
'''
SELECT Description
FROM stops
WHERE stops.Busstopcode = ?
'''

}

class dataStore:
    def createdb(self,db):
        db = sqlite3.connect(db)
    
    def createtable(self,db,table):
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(commands.get(table))
        conn.commit()
    
    def insert(self,data,db):
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        for stop in data:
            cur.execute(commands.get('bus_insert'),(stop['BusStopCode'],stop['RoadName'],stop['Description'],stop['Latitude'],stop['Longitude'],))
            conn.commit()
    
    def get_records(self,db,command,param=None):
        conn =  sqlite3.connect(db)
        cur = conn.cursor()
        if param is None:
            cur.execute(commands[command])
        else:
            cur.execute(commands[command],param)
        return cur.fetchall()
