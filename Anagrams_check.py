# Take input from user for two words, and check if they are anagrams
# (anagram example: listen and silent -> both contain the same number
# and set of alphabets)

def anagrams_check(word_first, word_second):
    word_first = word_first.replace(" ", "").lower()
    word_second = word_second.lower()

    if sorted(word_first) == sorted(word_second):
        print("Given words are anagrams")
    else:
        print("Given words are not anagrams")

word_first = input("Enter the first word: ")
word_second = input("Enter the second word:")

anagrams_check(word_first, word_second)