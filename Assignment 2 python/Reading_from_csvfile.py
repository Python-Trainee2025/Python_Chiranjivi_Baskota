# Read a .csv file and print each row. Handle file not found and other parsing errors if needed

import csv

try:
    filename = input("Enter the CSV file name (with .csv extension):")

    with open(filename, 'r') as file:
        reader = csv.reader(file)

        print("\nContents of the CSV file:")
        for row in reader:
            print(row)

except FileNotFoundError:
    print("Error: The file you entered does not exist. Please check the file name and try again.")

except csv.Error:
    print("Error: There was a problem parsing the CSV file.")