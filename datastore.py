import sqlite3

commands = {
'bus_stops':
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
INSERT OR IGNORE INTO stops VALUES(?,?,?,?,?);
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

class DataStore:
    def createdb(self,db):
        '''
        Create a database

        Args:
            db (database): Name of database to be created
        '''
        db = sqlite3.connect(db)
    
    def createtable(self,db,table):
        '''
        Creates a table in the specified database

        Args:
            db (database): Database to create the table in
            table (table): The table to create; command obtained from the 'commands' dictionary
        
        '''
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(commands.get(table))
        conn.commit()
    
    def coord_insert(self,data,db):
        """
        A function that inserts bus stops data into the 'STOPS' table

        Args:
            data (array): List containing bus stop data
            db (database): Database to insert the data into

        """
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        for stop in data:
            cur.execute(commands.get('bus_insert'),(stop['BusStopCode'],stop['RoadName'],stop['Description'],stop['Latitude'],stop['Longitude'],))
            conn.commit()
    
    def get_records(self,db,command,param=None):
        """
        A general function that retrieves records from a database

        Args:
            db (database): database to access
            command (string): key of one of the items in the commands dict
            param (tuple, optional): A tuple containing the items to be passed into the SQL command. Defaults to None.

        Returns:
            list: list of tuples containing the records retrieved
        """        
        conn =  sqlite3.connect(db)
        cur = conn.cursor()
        if param is None:
            cur.execute(commands[command])
        else:
            cur.execute(commands[command],param)
        return cur.fetchall()
