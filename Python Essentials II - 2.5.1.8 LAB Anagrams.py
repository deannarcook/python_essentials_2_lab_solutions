"""
Scenario
An anagram is a new word formed by rearranging the letters of a word, using all the original letters exactly once. For example, the phrases "rail safety" and "fairy tales" are anagrams, while "I am" and "You are" are not.

Your task is to write a program which:

asks the user for two separate texts;
checks whether, the entered texts are anagrams and prints the result.
Note:

assume that two empty strings are not anagrams;
treat upper- and lower-case letters as equal;
spaces are not taken into account during the check - treat them as non-existent
Test your code using the data we've provided.

Test data
Sample input:
Listen
Silent

Sample output:
Anagrams


Sample input:
modern
norman

Sample output:
Not anagrams
"""

text1 = input("Enter text: ")
text2 = input("Enter second text: ")

# define function to check if text is an anagram
def isAnagram(text1,text2):
# convert text to uppercase, remove spaces, and sort characters
    newText1 = sorted(text1.upper().replace(" ",""))
    newText2 = sorted(text2.upper().replace(" ",""))
    
# create variable to store the length of newText1 and newText2
    lengthNewText1 = len(newText1)
    lengthNewText2 = len(newText2)

# create variable to store index
    i = 0

# check if newText1 or newText2 variables are an empty string.
# check if length of newText1 and newText2 are the same
# if true set isAnagramResult to False
    if newText1 == "" or newText2 == "" or lengthNewText1 != lengthNewText2:
        isAnagramResult = False
    else:
# for each character in newText1, check if the character is equal to the character at the same index in newText2
# if true set isAnagramResult to True
# else set isAnagramResult to False and break loop
        for char in newText1:
            if char == newText2[i]:
                isAnagramResult = True
            else:
                isAnagramResult = False
                break
# increment i
            i += 1

# return isAnagramResult
    return isAnagramResult

# if isAnagram function returns True print "It's a anagram"
# else print "It's not a anagram"
if isAnagram(text1,text2) == True:
    print("It's a anagram")
else:
    print("It's not a anagram")