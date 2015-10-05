__author__ = 'Simon'
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        bottom = len(digits) - 1
        digits[bottom] += 1
        while bottom >= 0:
            if digits[bottom] == 10:
                if bottom == 0:
                    digits[bottom] = 0
                    digits.insert(0, 1)
                    break
                else:
                    digits[bottom] = 0
                    digits[bottom - 1] += 1
                    bottom = bottom - 1
            else:
                break
        return digits
