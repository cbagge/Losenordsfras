# As to not butcher our proud å, ä and ö:s
import unicodecsv as csv
# For stripping accents
import unicodedata

# File to be massaged
file="//nas3/users$/carlba/Documents/GitHub/L-senordsfras/Wordlist/SALDO/saldo20v03_subset.txt"

# Criteria
maxWordLength = 12
minWordLength = 3

# Method for stripping of accents we don't want in our passphrases
def strip_accents(string, accents=('COMBINING ACUTE ACCENT', 'COMBINING GRAVE ACCENT', 'COMBINING TILDE')):
    accents = set(map(unicodedata.lookup, accents))
    chars = [c for c in unicodedata.normalize('NFD', string) if c not in accents]
    return unicodedata.normalize('NFC', ''.join(chars))

# Open file and iterate through each line, extracting the word
# if it fits our criteria
with open(file, "rb") as tsvFile:
    # To use with our lazy duplicate check
    previousWord = ""
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
        word = strip_accents(word)

        # Lazy check for duplicate in our ordered dictionary.
        # Also, lower all the cases
        word = word.lower()
        if word == previousWord: continue
        previousWord = word

        # only the fittest survive! Print word
        print(word)




