import calendar
"""
Objectives
Improving the student's skills in using the Calendar class.
Scenario
During this course, we looked at the Calendar class a bit. Your task is to extend its functionality with a new method called count_weekday_in_year, which takes a year and a weekday as parameters, and then returns the number of occurrences of a specific weekday in the year.

Use the following tips:

Create a class called MyCalendar that extends the Calendar class;
create the count_weekday_in_year method with the year and weekday parameters. The weekday parameter should be a value between 0-6, where 0 is Monday and 6 is Sunday. The method should return the number of days as an integer;
in your implementation, use the monthdays2calendar method of the Calendar class.
The following are the expected results:

Sample arguments

year=2019, weekday=0

Expected output

52


Sample arguments

year=2000, weekday=6

Expected output

53


"""
# create calendar class so that we can make a subclass from it
class Calendar:
    pass

# create MyCalendar class as a subclass of the Calendar class
class MyCalendar(Calendar):
    # MyCalendar class constructor
    def __init__(self):
        # Calendar class constructor
        Calendar.__init__(self)

    # string method for returning results when MyCalendar class count_weekday_in_year method is called
    def __str__(self,result):
        # convert result parameter to string and output to console
        print(str(result))

    # create count_weekday_in_year method - accepts two arguments
    def count_weekday_in_year(self,year,weekday):
        # assign arguments to variables
        y = year
        #print('t - year: ' + str(year))
        wd = weekday
        #print('t - weekday: ' + str(wd))

        # create calendar object
        cal = calendar.Calendar()
        # create variable to count how many times the weekday argument occures
        weekday_counter = 0

        # loop through each month of the year
        for month in range(12):
            # create month variable that is month + 1 to account for the fact that range starts at 0 but int months
            # start at 1
            month += 1
            #print('t - month: ' + str(month))
            # loop through weeks that are part of the current month being processed
            for week in cal.monthdays2calendar(y,month):
                #print('t - week: ',end= '')
                #print(week)
                # loop through each day in the week for the month being processed
                for day in week:
                    # if the day of the week as an int (day[1[]) is equal to the weekday argument and the calendar
                    # day is not 0 (calendar days that are 0 are days that are not part of the month argument provided
                    # to monthdays2calendar, increment weekday_counter
                    if day[1] == wd and day[0] != 0:
                        weekday_counter += 1
                #print('t - weekday counter: ' + str(weekday_counter))

        # call __str__ method
        self.__str__(weekday_counter)

# create object from MyCalendar class
obj = MyCalendar()

# call count_weekday_in_year method from object
obj.count_weekday_in_year(2000,6)



