"""

Scenario
Let's play a game. We will give you two strings: one being a word (e.g., "dog") and the second being a combination of any characters.

Your task is to write a program which answers the following question: are the characters comprising the first string hidden inside the second string?

For example:

if the second string is given as "vcxzxduybfdsobywuefgas", the answer is yes;
if the second string is "vcxzxdcybfdstbywuefsas", the answer is no (as there are neither the letters "d", "o", or "g", in this order)
Hints:

you should use the two-argument variants of the pos() functions inside your code;
don't worry about case sensitivity.
Test your code using the data we've provided.

Test data
Sample input:
donor
Nabucodonosor

Sample output:
Yes


Sample input:
donut
Nabucodonosor

Sample output:

No

"""

# prompt user for two strings. convert string to upper case
firstString = input("Enter the first string: ").upper()
secondString = input("Enter the second string: ").upper()

# define function that determines if the characters in the first string can be found in the second string
def findAWord(firstString,secondString):
# variable used to track the last index where a character from the firstString was found in the secondString
    currentIndex = 0
# loop through first string
    for character in firstString:
# check if the character from firstString can be found in secondString
# start search at the last index that the loop found a character from the firstString in the secondString
        findFunctionResult = secondString.find(character,currentIndex)
# if character is not found return "No"
        if findFunctionResult == -1:
            return "No"
# else set currentIndex equal to findFunctionResult and restart loop
        else:
            currentIndex = findFunctionResult
    return "Yes"

print(findAWord(firstString,secondString))