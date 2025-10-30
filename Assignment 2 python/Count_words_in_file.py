# Read a text file and count the number of words in it.
# Handle the case where the file might not exist.

try:
    filename = input("Enter the file name:")

    with open(filename, "r") as file:
        content = file.read()
        words = content.split()
        print("Number of words in file: ", len(words))

except FileNotFoundError:
    print("Error: The file you entered does not exist.")