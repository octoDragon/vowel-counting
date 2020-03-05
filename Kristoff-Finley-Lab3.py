# --------------------------------------
# CSCI 127, Lab 3                      |
# September 17, 2019                   |
# Kristoff Finley                         |
# -------------------------------------- 
# Calculate how many vowels are in a   |
# sentence using three techniques.     |
# --------------------------------------

def count_built_in(sentence):
    vowels = "A", "E", "I", "O", "U", "a", "e", "i", "o", "u"
    total_vowels = 0
    for char in vowels:
        count_number = sentence.count(char)
        total_vowels +=count_number 
    return total_vowels
    
def count_iterative(sentence):
    vowels = "A", "E", "I", "O", "U", "a", "e", "i", "o", "u"
    total_vowels = 0
    for  char in sentence:
        if char in vowels:
            total_vowels += 1
    return total_vowels 

def count_recursive(sentence):
    vowel = "A", "E", "I", "O", "U", "a", "e", "i", "o", "u"
    sentence_leangth = len(sentence)
    if sentence_leangth == 0:               #Base Case 1 
        return 0 
    elif sentence_leangth > 0:
        for char in sentence:
            if char in vowel:           #General Case 1 
                sentence = sentence[1:]
                return 1+count_recursive(sentence)
            else:                                           #General Case 2 
                sentence = sentence[1:]
                return count_recursive(sentence)

# --------------------------------------

def main():
    answer = "yes"
    while (answer == "yes") or (answer == "y"):
        sentence = input("Please enter a sentence: ")
        sentence = sentence.lower()
        print()
        print("Calculating the number of vowels  using ...")
        print("-------------------------------------------")
        print("Built-in function =", count_built_in(sentence))
        print("Iteration =", count_iterative(sentence))
        print("Recursion =", count_recursive(sentence))
        print()
        answer = input("Would you like to continue: ").lower()
        print()

# --------------------------------------

main()
