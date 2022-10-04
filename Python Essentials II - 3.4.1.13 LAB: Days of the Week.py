"""
Objectives
improving the student's skills in defining classes from scratch;
defining and using instance variables;
defining and using methods.
Scenario
Your task is to implement a class called Weeker. Yes, your eyes don't deceive you – this name comes from the fact that objects of that class will be able to store and to manipulate the days of the week.

The class constructor accepts one argument – a string. The string represents the name of the day of the week and the only acceptable values must come from the following set:

Mon Tue Wed Thu Fri Sat Sun

Invoking the constructor with an argument from outside this set should raise the WeekDayError exception (define it yourself; don't worry, we'll talk about the objective nature of exceptions soon). The class should provide the following facilities:

objects of the class should be "printable", i.e. they should be able to implicitly convert themselves into strings of the same form as the constructor arguments;
the class should be equipped with one-parameter methods called add_days(n) and subtract_days(n), with n being an integer number and updating the day of week stored inside the object in the way reflecting the change of date by the indicated number of days, forward or backward.
all object's properties should be private;
Complete the template we've provided in the editor and run your code and check whether your output looks the same as ours.

Expected output
Mon
Tue
Sun
Sorry, I can't serve your request.

"""


class WeekDayError(Exception):
    pass


class Weeker:

    def __init__(self, day):
        self.__day = day
        # define list variable to store days of the week
        self.__daysOfTheWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        # define variable to store the index of the day after adding/subtracting days
        self.__newDayIndex = 0
        # verify that user provided day is valid
        if (self.__day)  in self.__daysOfTheWeek:
            # if day is valid create a variable storing the index of the day in __daysOfTheWeek
            self.__currentDayIndex = self.__daysOfTheWeek.index(self.__day)
        else:
            raise WeekDayError

    def __str__(self):
        return self.__day

    def add_days(self, n):
        self.__daysToAdd = n
        self.__daysToAdd = self.__daysToAdd % 7
        if self.__daysToAdd == 0:
            self.__str__()
        else:
            self.__newDayIndex = self.__currentDayIndex + self.__daysToAdd
            # update __day to be the day of the week after adding days
            self.__day = self.__daysOfTheWeek[self.__newDayIndex]

        self.__str__()

    def subtract_days(self, n):
        self.__daysToAdd = n
        self.__daysToAdd = self.__daysToAdd % 7
        if self.__daysToAdd == 0:
            self.__str__()
        else:
            self.__newDayIndex = self.__currentDayIndex - self.__daysToAdd + 1
            # update __day to be the day of the week after subtracting days
            self.__day = self.__daysOfTheWeek[self.__newDayIndex]

try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
