# Create a dictionary with a person's name and contact info for a small
# company, take the input from a user to search for a user using their name,
# return the number (example user will search for
# 'Ram' and if user exists, their phone number is returned)


employee_info = {
    "Chiranjivi Baskota": "9850000000",
    "Apar Sharma": "986000000",
    "Suman Sapkota": "9870000000",
    "Sudip Bhandari": "9880000000"
}

employee_name = input("Enter the employee name:")

employee_number = employee_info.get(employee_name)

if employee_number is not None:
    print("The employee number is", employee_number)
else:
    print("No such employee exists")
