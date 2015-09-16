__author__ = 'Simon'
class Solution(object):
    def isHappy(self, n):
        if n == 1:
            return n == 1
        check = []
        check.append(n)
        sum = 0
        num = n
        index = 0
        while sum != 1:
            while num >= 1:
                index = num % 10
                sum = sum + index * index
                num = num / 10
            if sum == 1:
                return sum == 1
            if sum in check:
                return sum == 1
            if sum not in check:
                check.append(sum)
                num = sum
                sum = 0
        return sum == 1