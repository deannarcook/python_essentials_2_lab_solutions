"""
Objectives
improving the student's skills in operating with files (reading)
using data collections for counting numerous data.
Scenario
A text file contains some text (nothing unusual) but we need to know how often (or how rare) each letter appears in the text. Such an analysis may be useful in cryptography, so we want to be able to do that in reference to the Latin alphabet.

Your task is to write a program which:

asks the user for the input file's name;
reads the file (if possible) and counts all the Latin letters (lower- and upper-case letters are treated as equal)
prints a simple histogram in alphabetical order (only non-zero counts should be presented)
Create a test file for the code, and check if your histogram contains valid results.

Assuming that the test file contains just one line filled with:

aBc
samplefile.txt

the expected output should look as follows:

a -> 1
b -> 1
c -> 1
output

Tip: We think that a dictionary is a perfect data collection medium for storing the counts. The letters may be keys while the counters can be values.
"""

from os import strerror

# create samplefile.txt
writeSrcFile = open("/Users/deannacook/Desktop/Python/PCAP/LAB/Module 4/samplefile.txt","w")
# write text to file
writeSrcFile.write('azBQca')
# close file
writeSrcFile.close()

# prompt user to input file name
srcFileName = input("Enter the source file's name: ")

# try to open file
try:
    srcFile = open("/Users/deannacook/Desktop/Python/PCAP/LAB/Module 4/" + srcFileName,"r")
# if an IOError exception is raised print error message
except IOError as e:
    print("I/O Error occurred: " + strerror(e.errno))

# create empty dictionary
histogramDic = {}

# for each line in srcFile
for line in srcFile:
# for each character in line
    for ch in line:
# if lowercase character is in the historgramDic
        if ch.lower() in histogramDic:
            # increment value
            newValue = histogramDic[ch] + 1
            # update key,value in histrogramDic
            histogramDic.update({ch:newValue})
# if lowercase character does not exist in histrogramDic add key,value to histogramDic
        else:
            histogramDic.update({ch.lower():1})

# sort keys in histogramDic alphabetically
sortedKeys = sorted(histogramDic.keys())

# for each key in sortedKeys print the key and the value associated with the key in histogramDic
for key in sortedKeys:
    print(key, "-->", histogramDic[key])





