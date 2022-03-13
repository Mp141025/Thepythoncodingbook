

import string

####
# read the data with 'with' we need not to close it , it automatically closes the file just opened

with open(r"D:\Priya Mishra\am\pride_and_prejudice.txt") as file:
    text = file.read()

#clean the data
text.lower()

words = text.split()
#print(words)
# Clean data by removing capital letters and punctuation marks
text = text.lower()
for punctuation_mark in string.punctuation:
    text = text.replace(punctuation_mark, " ")

# in order to have list of words we use split() function
words = text.split()

####
#  finding words and their freq
word_freq = {}


for w in words:
    if w not in word_freq.keys():
        word_freq[w] = 1
    else:
        word_freq[w] += 1

####
# Export to a CSV spreadsheet
'''with open("words in Pride and Prejudice.csv", "w") as file:
    
    file.write("Word,Frequency\n")

    
    for key, value in word_freq.items():
        file.write(f"{key},{value}\n")'''
# sorting of word freq as per the frequency of the word.
l=list(word_freq.values())
print(l)

l.sort()
print(l)
sorted(word_freq.values())
sorted(word_freq.items())
sortedwf={k:v for k,v in sorted(word_freq.items(), key= lambda v: v[1])}

print(sortedwf) ###########  Required answer <<<<<<<<<<<<<<<<<<<<

# difficult to visulize therefore colored
red = "\033[1;31m"
blue = "\033[1;34m"
green = "\033[1;32m"
no_color = "\033[0m"

for key in sortedwf.keys () :
    print ("(",red, key,",", blue, sortedwf[key],")")


