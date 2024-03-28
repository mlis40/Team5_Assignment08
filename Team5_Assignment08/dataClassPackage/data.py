# dataClassPackage.oy
# Name: Matthew Lisowsky and Harrison Moore (Team5)
# email: lisowsmd@mail.uc.edu and Moorehc@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: 3/28/2024
# Course/Section: IS4010-002
# Semester/Year: Spring 2024
# Brief Description of the assignment: In this Package we are connecting to the SQL server
# Citations:
# Anything else that's relevant:

# imports (ex: from functionPackage.functions import *)
import pyodbc 

# Harrison worked in the DataClass to get us connected to the database
class Data:
    def Connect(self):
        '''
        Connect to the database and create a cursor
        @return: the cursor object
        '''
        #Connection to the UC database 
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                              'Database=GroceryStoreSimulator;'
                              'uid=IS4010Login;'
                              'pwd=P@ssword2;')
        
        cursor = conn.cursor()
        return cursor