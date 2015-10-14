from sys import maxint

__author__ = 'Simon'
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = maxint

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)
        if x < self.min:
            self.min = x


    def pop(self):
        """
        :rtype: nothing
        """
        if self.stack[len(self.stack)-1] == self.min:
            self.min = maxint
            for i in range(len(self.stack)-1):
                if self.stack[i] < self.min:
                    self.min = self.stack[i]
        self.stack.pop(len(self.stack)-1)


    def top(self):
        """
        :rtype: int
        """
        return self.stack[len(self.stack)-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.min