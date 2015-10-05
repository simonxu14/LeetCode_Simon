__author__ = 'Simon'
class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = []


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue.append(x)


    def pop(self):
        """
        :rtype: nothing
        """
        length = len(self.queue)
        for i in range(length - 1):
            tmp = self.queue.pop()
            self.queue.append(tmp)
        self.queue.pop()


    def top(self):
        """
        :rtype: int
        """
        length = len(self.queue)
        for i in range(length):
            tmp = self.queue.pop()
            self.queue.append(tmp)
        return tmp


    def empty(self):
        """
        :rtype: bool
        """
        if self.queue:
            return False
        return True
