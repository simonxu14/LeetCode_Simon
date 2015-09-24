__author__ = 'Simon'
class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        # self._stack.append(self._stack[len(self._stack)-1])
        # i = len(self._stack)-2
        # while i > 0:
        #     self._stack[i] = self._stack[i-1]
        # self._stack[0] = x
        self._stack.append(x)
        i = len(self._stack)-1
        index = 0
        while i > 0:
            index = self._stack[i]
            self._stack[i] = self._stack[i-1]
            self._stack[i-1] = index
            i -= 1


    def pop(self):
        """
        :rtype: nothing
        """
        self._stack.pop()


    def peek(self):
        """
        :rtype: int
        """
        return self._stack[len(self._stack)-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self._stack) == 0

