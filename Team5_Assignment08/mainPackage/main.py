# main.py
# Name: Matthew Lisowsky and Harrison Moore (Team5)
# email: lisowsmd@mail.uc.edu and Moorehc@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: 3/28/2024
# Course/Section: IS4010-002
# Semester/Year: Spring 2024
# Brief Description of the assignment: In this package we worked on the outputing the brands that Coke makes
# Citations:
# Anything else that's relevant:

# imports (ex: from functionPackage.functions import *)
from dataClassPackage.data import Data

# Matt worked on writing out the code for the main
if __name__ == "__main__": #Entry point

    # Instantiate an object of type Data
    myData =  Data()
    # Invoke the connect method and store what it returns in another variable
    # Matt worked on the SQL Statement
    myCursor = myData.Connect() 
    
    myCursor.execute('SELECT DISTINCT tBrand.Brand, tProduct.ManufacturerID FROM  tBrand INNER JOIN tProduct ON tBrand.BrandID = tProduct.BrandID INNER JOIN tManufacturer ON tProduct.ManufacturerID = tManufacturer.ManufacturerID WHERE (tProduct.ManufacturerID = 13)') # Submit a query to the SQL Server instance and store the results in the cursor object


    # Harrison worked on writing out the sentence for the output
    print("Coca-Cola manufactures all of these brands: ") #Statement in front of data
    for row in myCursor: 
        print(row[0]); #Prints just the first column of data from the database, excluding the brand ID from the results 
        
