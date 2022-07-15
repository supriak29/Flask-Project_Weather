import sqlite3

class DatabaseConfig:
    ''''
        This class 
            - initializes Database name sent.
            - creates connection with database and sqlite3 server
            - create connection for server
            - commit the changes: connection in this case
            - close the connection()
    '''
    def __init__(self, databaseName=None):      # constructor which initailizes the db name
        self.databaseName = databaseName
    
    def createConnection(self):
        databaseName = '.'.join((str(self.databaseName),'db')) # db here is the extension we are providing our database file name
        print(databaseName) # prints the database name along with extension
        connection = sqlite3.connect(databaseName)  # connect with database
        cursor = connection.cursor() # create connection with cursor
        return connection, cursor  

    def commitClose(self):   # commiting the changes & closing the connection
        connection, cursor = self.createConnection() 
        connection.commit()
        connection.close()
