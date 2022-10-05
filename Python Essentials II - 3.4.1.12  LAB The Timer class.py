""""
Objectives
improving the student's skills in defining classes from scratch;
defining and using instance variables;
defining and using methods.
Scenario
We need a class able to count seconds. Easy? Not as much as you may think as we're going to have some specific expectations.

Read them carefully as the class you're about write will be used to launch rockets carrying international missions to Mars. It's a great responsibility. We're counting on you!

Your class will be called Timer. Its constructor accepts three arguments representing hours (a value from range [0..23] - we will be using the military time), minutes (from range [0..59]) and seconds (from range [0..59]).

Zero is the default value for all of the above parameters. There is no need to perform any validation checks.

The class itself should provide the following facilities:

objects of the class should be "printable", i.e. they should be able to implicitly convert themselves into strings of the following form: "hh:mm:ss", with leading zeros added when any of the values is less than 10;
the class should be equipped with parameterless methods called next_second() and previous_second(), incrementing the time stored inside objects by +1/-1 second respectively.
Use the following hints:

all object's properties should be private;
consider writing a separate function (not method!) to format the time string.
Complete the template we've provided in the editor. Run your code and check whether the output looks the same as ours.

Expected output
23:59:59
00:00:00
23:59:59
"""

class Timer:
    def __init__(self, hrs = 0, mins = 0, secs = 0):
        # initialize hrs, mins, and secs variables
        self.__hrs = hrs
        self.__mins = mins
        self.__secs = secs

    def __str__(self):
        # converts hrs, mins, and secs to strings
        # concatenate into one string separated by '-'
        self.__lst = str(self.__hrs) + '-' +  str(self.__mins) + '-' + str(self.__secs)

        # create a list of hrs, mins, and secs variables
        self.__lst = self.__lst.split('-')

        i = 0

        # for each hrs/mins/secs in __list check if the length is 1
        # if yes pre-pend 0
        for t in self.__lst:
            if len(t) == 1:
                self.__lst[i] = '0' + t
            i += 1

        # return time in hh:mm:ss format
        return ':'.join(self.__lst)

    def next_second(self):
        # increment secs
        self.__secs += 1

        # if secs is 60 set secs to 0 and increment mins
        if self.__secs == 60:
            self.__secs = 0
            self.__mins += 1
            # if mins is 60 set mins to 0 and increment hrs
            if self.__mins == 60:
                self.__mins = 0
                self.__hrs += 1
                # if hrs is 24 set hrs to 0
                if self.__hrs == 24:
                    self.__hrs = 0

        return self.__str__

    def prev_second(self):
        # decrement secs
        self.__secs -= 1

        # if secs is -1 set secs to 59 and decrement mins
        if self.__secs == -1:
            self.__secs = 59
            self.__mins -= 1
            # if mins is -1 set mins to 59 and decrement hrs
            if self.__mins == -1:
                self.__mins = 59
                self.__hrs -= 1
                # if hrs is -1 set hrs to 23
                if self.__hrs == -1:
                    self.__hrs = 23
        return self.__str__


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
