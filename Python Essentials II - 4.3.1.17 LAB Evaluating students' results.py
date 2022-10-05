import os

"""
Objectives
improve the student's skills in operating with files (reading)
perfecting the student's abilities in defining and using self-defined exceptions and dictionaries.
Scenario
Prof. Jekyll conducts classes with students and regularly makes notes in a text file. Each line of the file contains three elements: the student's first name, the student's last name, and the number of point the student received during certain classes.

The elements are separated with white spaces. Each student may appear more than once inside Prof. Jekyll's file.

The file may look as follows:

John	Smith	5
Anna	Boleyn	4.5
John	Smith	2
Anna	Boleyn	11
Andrew	Cox	1.5
samplefile.txt

Your task is to write a program which:

asks the user for Prof. Jekyll's file name;
reads the file contents and counts the sum of the received points for each student;
prints a simple (but sorted) report, just like this one:
Andrew Cox 	 1.5
Anna Boleyn 	 15.5
John Smith 	 7.0
output

Note:

your program must be fully protected against all possible failures: the file's non-existence, the file's emptiness, or any input data failures; encountering any data error should cause immediate program termination, and the erroneous should be presented to the user;
implement and use your own exceptions hierarchy - we've presented it in the editor; the second exception should be raised when a bad line is detect, and the third when the source file exists but is empty.
Tip: Use a dictionary to store the students' data.


 Sandbox
Code
class StudentsDataException(Exception):
pass


class BadLine(StudentsDataException):
# Write your code here.


class FileEmpty(StudentsDataException):
# Write your code here.
class StudentsDataException(Exception):


Console

"""

class StudentsDataException(Exception):
    def __init__(self):
        Exception.__init__(self)


class BadLine(StudentsDataException):
    def __init__(self):
        StudentsDataException.__init__(self)
    def __str__(self):
        print('The file contains a bad line of data.')

class FileEmpty(StudentsDataException):
    def __init__(self):
        SudentDataException.__init__(self)

    def __str__(self):
        print('The file is empty.')

ui_InputFileName = 'inputFile'
    #input('Enter the name of the file:')

inputFileName = ui_InputFileName + '.txt'

inputFilePath = '/Users/deannacook/Desktop/Python/PCAP/LAB/Module 4/' + inputFileName
writeFile = open(inputFilePath, 'w')
writeFile.write("John	Smith	5\nAnna	Boleyn	4.5\nJohn	Smith	2\nAnna	Boleyn	11\nAndrew	Cox	1.5")
writeFile.close()

try:
    inputFile = open(inputFilePath, 'r')
except Exception as exc:
    print('The file could not be opened - ' + os.strerror(exc.errno))

if os.stat(inputFilePath).st_size == 0:
    emptyFileIssue = FileEmpty()

studentPointsTracker = {}

for line in inputFile:
    #print(line.replace('\n',''))
    line = line.split()
    try:
        studentName = line[0] + ' ' + line[1]
        studentPoints = float(line[2])
    except:
        BadLineIssue = BadLine()
    else:
        #print(studentName + ' ' + studentPoints)
        if studentName in studentPointsTracker:
            studentPointsTracker.update({studentName: studentPointsTracker[studentName] + studentPoints})
        else:
            studentPointsTracker.update({studentName: studentPoints})

# define function that sorts data in dictionary
sortedKeys = sorted(studentPointsTracker.keys())

for i in sortedKeys:
    print(i + ' ' + str(studentPointsTracker[i]))


