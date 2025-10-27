# Get input from user and check if it is palindrome

input_taken = input("Enter any word or phrase")

def palindrome_check(input_taken):
    input_taken = input_taken.replace(" ", "").lower()

    if input_taken == input_taken[::-1]:
        print("The entered word/phrase is palindrome")
    else:
        print("The entered word/phrase is not palindrome")

palindrome_check(input_taken)