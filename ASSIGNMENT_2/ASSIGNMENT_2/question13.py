''' Create a function called word_intersection that prompts the user for two English words, and displays which letters the two words have in common. '''
def word_intersection():
    word1 = input("Enter first word: ")
    word2 = input("Enter second word: ")
    common_letters = set(word1) & set(word2)
    print("Common letters:", common_letters)

word_intersection()
