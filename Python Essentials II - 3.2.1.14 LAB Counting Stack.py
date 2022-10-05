"""
Objectives
improve the student's skills in defining classes;
using existing classes to create new classes equipped with new functionalities.
Scenario
We've showed you recently how to extend Stack possibilities by defining a new class (i.e., a subclass) which retains all inherited traits and adds some new ones.

Your task is to extend the Stack class behavior in such a way so that the class is able to count all the elements that are pushed and popped (we assume that counting pops is enough). Use the Stack class we've provided in the editor.

Follow the hints:

introduce a property designed to count pop operations and name it in a way which guarantees hiding it;
initialize it to zero inside the constructor;
provide a method which returns the value currently assigned to the counter (name it get_counter()).
Complete the code in the editor. Run it to check whether your code outputs 100.
"""

class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
# call cosntructor from Stack class
        Stack.__init__(self)
# create new private variable to track the number of pops
        self.__countPops = 0

    def get_counter(self):
# make the private __countPops variable accessible from outside of the class by creating a function that returns the
# value of the variable.
        return self.__countPops

# overwrite the pop function
    def pop(self):
# set val equal to the pop method from the Stack class
        val = Stack.pop(self)
# increment the __countPops variable
        self.__countPops += 1
        return val

stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())
