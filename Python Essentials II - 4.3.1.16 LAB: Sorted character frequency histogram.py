"""
Level of difficulty
Medium

Prerequisites
4.3.1.15

Objectives
improve the student's skills in operating with files (reading/writing)
using lambdas to change the sort order.
Scenario
The previous code needs to be improved. It's okay, but it has to be better.

Your task is to make some amendments, which generate the following results:

the output histogram will be sorted based on the characters' frequency (the bigger counter should be presented first)
the histogram should be sent to a file with the same name as the input one, but with the suffix '.hist' (it should be concatenated to the original name)
Assuming that the input file contains just one line filled with:

cBabAa
samplefile.txt

the expected output should look as follows:

a -> 3
b -> 2
c -> 1
output

Tip: Use a lambda to change the sort order.
"""

from os import strerror

# create samplefile.txt
writeSrcFile = open("/Users/deannacook/Desktop/Python/PCAP/LAB/Module 4/samplefile.txt","w")
# write text to file
writeSrcFile.write('cBabAa')
# close file
writeSrcFile.close()

# prompt user to input file name
userInputSrcFileName = input("Enter the source file's name: ")
srcFileName = userInputSrcFileName + ".txt"

# try to open file
try:
    srcFile = open("/Users/deannacook/Desktop/Python/PCAP/LAB/Module 4/" + srcFileName ,"r")
# if an IOError exception is raised print error message
except IOError as e:
    print("I/O Error occurred: " + strerror(e.errno))

# create empty dictionary
histogramDic = {}

# for each line in srcFile
for line in srcFile:
# for each character in line
    for ch in line:
        ch = ch.lower()
# if lowercase character is in the historgramDic
        if ch in histogramDic:
            # update key,value in histrogramDic
            histogramDic.update({ch:histogramDic[ch] + 1})
# if lowercase character does not exist in histrogramDic add key,value to histogramDic
        else:
            histogramDic.update({ch:1})

# define function that sorts data in dictionary
def sortDictionary(dict):
# sort data based on value desc
        sortedKeys = sorted(dict.items(),key = lambda item: item[1], reverse = True)
        return sortedKeys

# create variable storing output file name
outputFileName = userInputSrcFileName + ".hist"

# try to open file
try:
    outputFile = open("/Users/deannacook/Desktop/Python/PCAP/LAB/Module 4/" + outputFileName,"w")
# if an IOError exception is raised print error message
except IOError as e:
    print("I/O Error occurred: " + strerror(e.errno))

# for each key in sortedKeys print the key and the value associated with the key in histogramDic
for item in sortDictionary(histogramDic):
    outputLine = item[0] +  " -> " + str(item[1]) + "\n"
    outputFile.write(outputLine)

# close files
srcFile.close()
outputFile.close()









