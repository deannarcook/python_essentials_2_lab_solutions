"""
You are already familiar with the Caesar cipher, and this is why we want you to improve the code we showed you recently.

The original Caesar cipher shifts each character by one: a becomes b, z becomes a, and so on. Let's make it a bit harder, and allow the shifted value to come from the range 1..25 inclusive.

Moreover, let the code preserve the letters' case (lower-case letters will remain lower-case) and all non-alphabetical characters should remain untouched.

Your task is to write a program which:

asks the user for one line of text to encrypt;
asks the user for a shift value (an integer number from the range 1..25 - note: you should force the user to enter a valid shift value (don't give up and don't let bad data fool you!)
prints out the encoded text.
Test your code using the data we've provided.

Test data
Sample input:
abcxyzABCxyz 123
2

Sample output:
cdezabCDEzab 123

Sample input:
The die is cast
25

Sample output:
Sgd chd hr bzrs

"""
# create variable containing user input for text to encrypt
text = str(input("Enter text to encrypt: "))
# create variable containing user input for shiftValue. cast to string.
shiftValue = str(input("Enter a shift value - the shift value must be an integer between 1 and 25: "))
# create variable to store encrypted text
encryptedText = ""
#
unencryptedText = ""

"""
print("test: " + str(shiftValue.isnumeric()))
print("test: " + str(int(shiftValue) < 1))
print("test: " + str(int(shiftValue) > 25))
"""

# validate user input
while not shiftValue.isnumeric() or int(shiftValue) < 1 or int(shiftValue) > 25:
    shiftValue = input("You've entered an invalid value. Enter a shift value - the shift value must be an integer between 1 and 25: ")

# define shiftValueInt variable containing shiftValue as an int
shiftValueInt = int(shiftValue)

#print("test - ord z: " + str(ord("z")))
#print("test - ord a: " + str(ord("a")))
#print("test - ord Z: " + str(ord("Z")))
#print("test - ord A: " + str(ord("A")))

# iterate through each character in user's input
for char in text:
    #print("test: " + char)
# if character is not an alphabet character skip
    if ord(char) == 32:
        #print("test - Appending space to encryptedTest")
        encryptedText += char
        continue
    elif char.isnumeric():
        encryptedText += char
        continue
# create variable called code - store the ASCII code for the character
    code = ord(char)
    #print("test - code: " + str(code))
# create variable called encryptedCode - store the ASCII code for the character incremented by the user provided shift value
    encryptedCode = code + shiftValueInt
    #print("test - encryptedCode: " + str(encryptedCode))
    isupper = char.isupper()
    #print("test - isupper: " + str(isupper))
# if the encryptedCode is outside of the Latin alphabet set encryptedCode to the ASCII code for A
    if isupper == True and encryptedCode > ord("Z"):
        encryptedCode = ord("A") + (encryptedCode - ord("Z") - 1)
        #print("test - isupper is true scenario")
    if isupper == False and encryptedCode > ord("z"):
        encryptedCode = ord("a") + (encryptedCode - ord("z") - 1)
        #print("test - isupper is false scenario")
    #print("test - encryptedCode: " + str(encryptedCode))
# Append encryptedCode to encryptedText
    encryptedText += chr(encryptedCode)

print("Original Text:       " + text)
print("Encrypted Text:      " + encryptedText)

# iterate through each character in user's input
for char in encryptedText:
    # print("test: " + char)
# if character is not an alphabet character skip
    if ord(char) == 32:
        #print("test - Appending space to encryptedTest")
        unencryptedText += char
        continue
    elif char.isnumeric():
        unencryptedText += char
        continue
# create variable called code - store the ASCII code for the character
    code = ord(char)
    #print("test - code: " + str(code))
# create variable called encryptedCode - store the ASCII code for the character incremented by the user provided shift value
    unencryptedCode = code - shiftValueInt
    #print("test - unencryptedCode: " + str(unencryptedCode))
    isupper = char.isupper()
    #print("test - isupper: " + str(isupper))
# if the encryptedCode is outside of the Latin alphabet set encryptedCode to the ASCII code for A
    if isupper == True and unencryptedCode < ord("A"):
        unencryptedCode = ord("Z") - (ord("A") - 1 - unencryptedCode)
        #print("test - isupper is true scenario")
    if isupper == False and unencryptedCode < ord("a"):
        unencryptedCode = ord("z") - (ord("a") - 1 - unencryptedCode)
        #print("test - isupper is false scenario")
    #print("test - unencryptedCode: " + str(unencryptedCode))
# Append encryptedCode to encryptedText
    unencryptedText += chr(unencryptedCode)

print("Unencrypted Text:    " + unencryptedText)