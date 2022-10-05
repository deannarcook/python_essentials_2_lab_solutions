"""
Objectives
improving the student's skills in defining subclasses;
adding a new functionality to an existing class.
Scenario
Your task is to slightly extend the Queue class' capabilities. We want it to have a parameterless method that returns True if the queue is empty and False otherwise.

Complete the code we've provided in the editor. Run it to check whether it outputs a similar result to ours.

Below you can copy the code we used in the previous lab:
"""

class QueueError(IndexError):  # Choose base class for the new exception.
    def __init__(self):
        IndexError.__init__(self)
        print("Queue error")

class Queue:
    def __init__(self):
    # create a list variable to store the queue items
        self.queueList = []

    def put(self, elem):
    # add elem to the end of the queue
        self.queueList.insert(0,elem)

    def get(self):
       val = self.queueList[-1]
       del self.queueList[-1]
       return val


class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)
        self.queueList = []

    def isempty(self):
        if len(self.queueList) > 0:
            return False
        else:
            return True

que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")



