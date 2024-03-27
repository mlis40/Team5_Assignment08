# dataClassPackage.oy
# The Data Class

# imports
import pyodbc

class Data:
    def Connect(self):
        '''
        Connect to the database and create a cursor
        @return: the cursor object
        '''
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                              'Database=GroceryStoreSimulator;'
                              'uid=IS4010Login;'
                              'pwd=P@ssword2;')
        
        cursor = conn.cursor()
        return cursor