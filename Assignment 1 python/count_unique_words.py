# Input a sentence or a paragraph from user and extract how many
# unique words are used and display the count

def count_unique_words(text):
    cleaned_char = []
    for char in text:
        if char.isalnum():
            cleaned_char.append(char.lower())
        elif char.isspace():
            cleaned_char.append(char)
        else:
            cleaned_char.append(" ")

    cleaned_text = "".join(cleaned_char)

    words = cleaned_text.split()
    unique_words = set(words)
    return len(unique_words)

user_input = input("Enter the text or paragraph:")

unique_counts = count_unique_words(user_input)

print(unique_counts)