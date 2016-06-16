"""

# Homework 1 (Spyhce) submission from Cristian Hainic -- IAP 1st year, 2nd semester

"""


import re

to_open = input("Enter the name of the file you'd like to parse. \
Make sure the file is in the root directory of the project!\n")

# I get my data as a list of strings with no punctuation marks
with open(str(to_open), "r") as file:
    words = file.read().split()
    words = ' '.join(words)
    no_punctuation = re.sub('[^\w ]', '', words)
    words = no_punctuation.split()

# Each word in the file will be a key in a dictionary.
# If the word has no anagrams in the file, its value in the dictionary will be an empty list
# If the word has anagrams in the file, its value in the dictionary will be a list containing all anagrams as strings.
anagrams = {}

# duplicate list against which I confront each sorted word in the original list
duplicate_words = words

# Let the parsing begin.
for k in words:
    anagrams[k] = []
    for i in duplicate_words:
        if ''.join(sorted(k)) == ''.join(sorted(i)):
            anagrams[k].append(i)

# I'm now deleting duplicate words stemming from the duplicate list\
# *AND* duplicate words stemming from the file itself, leaving only the anagrams
for k, v in anagrams.items():
    anagrams[k] = [i for i in v if i != k]


# preparing the output
def print_anagrams(a_dict):
    for k, v in a_dict.items():
        if v:
            print("Word '" + k + "' has " + str(len(v)) + " anagram(s) in the text: " + str(v) + ".")


def search_anagrams(query, a_dict):
    # old school linear search
    position = 0
    found = False
    while position < len(a_dict) and not found:
        for k, v in a_dict.items():
            if k == str(query):
                found = True
                if v:
                    print("Found " + str(len(v)) + " anagram(s) for " + str(query) + ": " + str(v) + ".")
                elif not v:
                    print("The word doesn't seem to have any anagrams in the text.")
        position += 1
    if found == False:
        print("The word you entered is not in the text.")

print("\nAnagrams found:")
print_anagrams(anagrams)

print("\nEnter a word you'd like to search anagrams for in the text:")
userinput = input("> ")
search_anagrams(userinput, anagrams)