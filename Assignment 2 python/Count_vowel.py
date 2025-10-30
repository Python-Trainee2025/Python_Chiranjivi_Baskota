# Accept a word/sentence from the user and count
# how many vowels (a, e, i, o, u) are present in it.


text = input("Enter any word:")

text = text.lower()

vowels = "aeiou"

count = 0

for char in text:
    if char in vowels:
        count += 1

print("Number of vowels:", count)