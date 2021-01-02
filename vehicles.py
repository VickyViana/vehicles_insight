#Pandas is imported
import pandas as pd

#Access to table vehicles
vehicles = pd.read_csv('data/vehicles.csv')

#Different options of information to be printed in console
print("""Choose the number of the option you need to know:
	1 - Shape of dataframe
	2 - Number of rows
	3 - Name of columns
	4 - Type of columns
	5 - Amount of Null values per column
	6 - Minimun value in each column
	7 - Maximun value in each column """)
	
choice = input("Please enter your option: ")
options = ['1','2','3','4','5','6','7']

while choice not in options:
	choice = input("Please introduce a number of option between 1 to 7: ")
	
if choice == '1':
	print(vehicles.shape)
elif choice == '2':
	print(len(vehicles))
elif choice == '3':
	print("Columns are: ", vehicles.columns)
elif choice == '4':
	print(vehicles.dtypes)
elif choice == '5':
	print(vehicles.isnull().sum())
elif choice == '6':
	print(vehicles.min())
elif choice == '7':
	print(vehicles.max())



