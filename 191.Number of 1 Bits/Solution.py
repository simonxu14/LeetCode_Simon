__author__ = 'Simon'
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary_str_n = bin(n)
        hamming_weight = binary_str_n.count('1')
        return hamming_weight