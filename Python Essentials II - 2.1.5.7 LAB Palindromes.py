"""
Scenario
Do you know what a palindrome is?

It's a word which look the same when read forward and backward. For example, "kayak" is a palindrome, while "loyal" is not.

Your task is to write a program which:
[x] asks the user for some text;
[x] checks whether the entered text is a palindrome, and prints result.

Note:

assume that an empty string isn't a palindrome;
treat upper- and lower-case letters as equal;
spaces are not taken into account during the check - treat them as non-existent;
there are more than a few correct solutions - try to find more than one.
Test your code using the data we've provided.

Test data
Sample input:
Ten animals I slam in a net

Sample output:
It's a palindrome


Sample input:
Eleven animals I slam in a net

Sample output:
It's not a palindrome
"""

text = input("Enter a word and I'll tell you if it's a palindrome: ")

# define function to check if text is a palindrome
def isPalindrome(text):
# convert text to uppercase and remove spaces
    newText = text.upper().replace(" ","")
# create variable to store the length of newText
    lengthNewText = len(newText)

# create variable storing the last index of the newText
    i = lengthNewText - 1

# check if newText variable is empty
    if newText == "":
        isPalindromeResult = False
    else:
# for each character in newText, check if the character is equal to the i
# if true set isPalindromeResult to True
# else set isPalindromeResult to False and break loop
        for char in newText:
            if char == newText[i]:
                isPalindromeResult = True
            else:
                isPalindromeResult = False
                break
# decrement i
            i -= 1

# return isPalindromeResult
    return isPalindromeResult

# if isPalindrome function returns True print "It's a palindrome"
# else print "It's not a palindrome"
if isPalindrome(text) == True:
    print("It's a palindrome")
else:
    print("It's not a palindrome")