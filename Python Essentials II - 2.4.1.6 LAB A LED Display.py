"""
Estimated time
30 minutes

Level of difficulty
Medium

Objectives
improving the student's skills in operating with strings;
using strings to represent non-text data.
Scenario
You've surely seen a seven-segment display.

It's a device (sometimes electronic, sometimes mechanical) designed to present one decimal digit using a subset of seven segments. If you still don't know what it is, refer to the following Wikipedia article.

Your task is to write a program which is able to simulate the work of a seven-display device, although you're going to use single LEDs instead of segments.

Each digit is constructed from 13 LEDs (some lit, some dark, of course) - that's how we imagine it:

  # ### ### # # ### ### ### ### ### ###
  #   #   # # # #   #     # # # # # # #
  # ### ### ### ### ###   # ### ### # #
  # #     #   #   # # #   # # #   # # #
  # ### ###   # ### ###   # ### ### ###

Note: the number 8 shows all the LED lights on.

Your code has to display any non-negative integer number entered by the user.

Tip: using a list containing patterns of all ten digits may be very helpful.

Test data
Sample input:

123

Sample output:

  # ### ###
  #   #   #
  # ### ###
  # #     #
  # ### ###

Sample input:

9081726354

Sample output:

### ### ###   # ### ### ### ### ### # #
# # # # # #   #   #   # #     # #   # #
### # # ###   #   # ### ### ### ### ###
  # # # # #   #   # #   # #   #   #   #
### ### ###   #   # ### ### ### ###   #

"""
# prompt user for input. store input in variable called usersInput
print()
userInput = input("Enter the number that you want to convert to seven digit display format: ")

# define variable containing userInput as a string
userInputString = str(userInput)
# define variable containing length of user's input
userInputLength = len(userInputString)
# print(userInputLength)
# define list variables containing digits represented in seven digit diplay format
one = ["  #","  #","  #","  #","  #"]
two = ["###","  #","###","#  ","###"]
three = ["###","  #","###","  #","###"]
four = ["# #","# #","###","  #","  #"]
five = ["###","#  ","###","  #","###"]
six = ["###","#  ","###","# #","###"]
seven = ["###","  #","  #","  #","  #"]
eight = ["###","# #","###","# #","###"]
nine = ["###","# #","###","  #","  #"]
zero = ["###","# #","# #","# #","###"]
# define empty list to store the user's input in seven digit display format
userInputList = []

# step 1: convert each digit in user's input to seven digit format + append to userInputList
# the result is a list of lists
for i in userInputString:
    if i == '1':
        userInputList.append(one)
    elif i == '2':
        userInputList.append(two)
    elif i == '3':
        userInputList.append(three)
    elif i == '4':
        userInputList.append(four)
    elif i == '5':
        userInputList.append(five)
    elif i == '6':
        userInputList.append(six)
    elif i == '7':
        userInputList.append(seven)
    elif i == '8':
        userInputList.append(eight)
    elif i == '9':
        userInputList.append(nine)
    elif i == '0':
        userInputList.append(zero)

# define empty list variables, one for each line of the seven digit display output
lineOne = []
lineTwo = []
lineThree = []
lineFour = []
lineFive = []

# define variable for while statement condition
digitsToPrint = userInputLength
# define counter variable for while statements.
j = 0

# step 2: populate list containing the first line of the seven digit display
while j < digitsToPrint:
    lineOne.append(userInputList[j][0])
    j += 1

# step 3: reset j counter variable. populate list containing the second line of the seven digit display
j = 0
while j < digitsToPrint:
    lineTwo.append(userInputList[j][1])
    j += 1

# step 4: reset j counter variable. populate list containing the third line of the seven digit display
j = 0
while j < digitsToPrint:
    lineThree.append(userInputList[j][2])
    j += 1

# step 5: reset j counter variable. populate list containing the fourth line of the seven digit display
j = 0
while j < digitsToPrint:
    lineFour.append(userInputList[j][3])
    j += 1

# step 6: reset j counter variable. populate list containing the fifth line of the seven digit display
j = 0
while j < digitsToPrint:
    lineFive.append(userInputList[j][4])
    j += 1

# step 7: print user input in seven digit display format

print(" ".join(lineOne))
print(" ".join(lineTwo))
print(" ".join(lineThree))
print(" ".join(lineFour))
print(" ".join(lineFive))
