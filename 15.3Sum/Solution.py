import collections

class Solution(object):
    def threeSum(self, nums):

        result = list()
        c = collections.Counter(nums)
        num = c.keys()

        for i in range(len(num)):
            number1 = num[i]
            if c[number1] > 1 and -2*number1 in c:
                if number1 < 0:
                    result.append([number1, number1, -2*number1])
                elif number1 > 0:
                    result.append([-2*number1, number1, number1])
            for j in range(i+1, len(num)):
                number2 = num[j]
                number3 = -(number1 + number2)
                if number3 > number2 and number3 > number1 and number3 in c:
                    result.append([min(number1, number2), max(number1, number2), number3])

        if c[0] > 2:
            result.append([0,0,0])

        return result

        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """