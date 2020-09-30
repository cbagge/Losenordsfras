# As to not butcher our proud å, ä and ö:s
import unicodecsv as csv
# For stripping accents
import unicodedata
# For entropy calculations
import math
# For path
import os

# File to be massaged
dir = os.path.dirname(__file__)
# Use a subset of complete dictionary, for development
#dictFile = os.path.join(dir, "SALDO", "saldo20v03_subset.txt")
# Full dictionary
dictFile = os.path.join(dir, "SALDO", "saldo20v03.txt")

# Output file
outputFile = os.path.join(dir, "wordlist.js")

#file="//nas3/users$/carlba/Documents/GitHub/L-senordsfras/Wordlist/SALDO/saldo20v03.txt"

# Criteria
maxWordLength = 12
minWordLength = 3
stripAccents = True

# Method for stripping of accents we don't want in our passphrases
def strip_accents(string, accents=('COMBINING ACUTE ACCENT', 'COMBINING GRAVE ACCENT', 'COMBINING TILDE')):
    accents = set(map(unicodedata.lookup, accents))
    chars = [c for c in unicodedata.normalize('NFD', string) if c not in accents]
    return unicodedata.normalize('NFC', ''.join(chars))

# Method for calculating per word entropy with our dictionary and returing a 6 char long string
def calc_entropy(int):
    return str(math.log(int) / math.log(2))[:6]

def read_dictionary():
    # Open file and iterate through each line, extracting the word
    # if it fits our criteria
    with open(dictFile, "rb") as tsvFile:
        # To use with our lazy duplicate check
        previousWord = ""
        # To keep track of dict size
        wordCount = 0
        # Our wordList
        wordList = list()

        for line in csv.reader(tsvFile,  encoding='utf-8', dialect="excel-tab"):
            # If it's a comment, get the next line
            if line[0][0] == "#": continue

            # Get the word from wordsoup
            word = line[0].split(".")[0]

            # If it's shorter than minWordLength, chuck it
            wordLength = len(word)
            if wordLength <= minWordLength: continue
            
            # If it's longer than  maxWordLength, toss it
            if wordLength >= maxWordLength: continue

            # If the word a multi word word, remove it
            if "_" in word: continue

            # Strip accents, those are not useful for passwords.
            if stripAccents: word = strip_accents(word)

            # Lazy check for duplicate in our ordered dictionary.
            # Also, lower all the cases
            word = word.lower()
            if word == previousWord: continue
            previousWord = word

            # Count our chickens
            wordCount += 1

            # only the fittest survive! 
            # Print word
            #print(word)
            # Add to list
            wordList.append(word)

        # Housekeeping
        tsvFile.close()
        return(wordCount, wordList)

def write_dictionary(outputFile, wordList):
    with open(outputFile, "w", encoding='utf8') as file:
        # Create header for our .js file
        file.write("var wordlist = [\n")

        # Iterate over our wordlist, except the last element, and build the output file
        for word in wordList[:-1]:
            file.write("'" + word + "',\n")

        # Write the last item and finishing touches
        file.write("'" + wordList[-1] + "'\n")
        file.write("];\n")

        # Housekeeping
        file.close()

def main():
    # Parse and clean our dictionary
    wordCount, wordList = read_dictionary()

    # Write passphrase dictionary
    write_dictionary(outputFile, wordList)

    print("")
    print("Word count in dicitionary: " + str(wordCount))
    print("Which gives our passphrase a secuity of " + calc_entropy(wordCount) + " bits per word in the passphrase")
    print("")

if __name__ == "__main__":
    main()

