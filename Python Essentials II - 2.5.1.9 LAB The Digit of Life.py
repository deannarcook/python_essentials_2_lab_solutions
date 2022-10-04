"""
Some say that the Digit of Life is a digit evaluated using somebody's birthday. It's simple - you just need to sum all the digits of the date. If the result contains more than one digit, you have to repeat the addition until you get exactly one digit. For example:

1 January 2017 = 2017 01 01
2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
1 + 2 = 3
3 is the digit we searched for and found.

Your task is to write a program which:

asks the user her/his birthday (in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY - actually, the order of the digits doesn't matter)
outputs the Digit of Life for the date.
Test your code using the data we've provided.

Test data
Sample input:

19991229

Sample output:

6


Sample input:

20000101

Sample output:

4
"""

# prompt user for birthday. store in variable called text.
text = input("Enter your birthday in the following format - YYYYMMDD,YYYYDDMM, or MMDDYYYY and I'll tell you your "
            "digit of life! ")


# function that computes digit of life
def computeDigitOfLife(birthday):
# create variables for day of life computatino
    digitOfLife = 0
    digitOfLifeTemp = 0
# for each digit in user's birthday, add the digit to digitOfLife
    for digit in birthday:
        digitOfLife += int(digit)

# if digitOfLife is one digit return digitOfLife
    if digitOfLife <= 9 and digitOfLife >= 0:
        return str(digitOfLife)
# else, while digitOfLife is greater than 9, iterate through digitOfLife and sum the digits.
    else:
        while int(digitOfLife) > 9:
            for digit in str(digitOfLife):
# store value in digitOfLifeTemp
                digitOfLifeTemp += int(digit)
                #print("test - digitOfLifeTemp: " + str(digit))
# set digitOfLife equal to digitOfLifeTemp
            digitOfLife = str(digitOfLifeTemp)
# reset DigitOfLife to 0
            digitOfLifeTemp = 0

        return str(digitOfLife)

print("Your digit of life is " + computeDigitOfLife(text))


