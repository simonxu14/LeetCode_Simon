__author__ = 'Simon'
class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit():
            return [int(input)]
        res = []
        for i in range(len(input)):
            if input[i] in "-+*":
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i+1:])
                for j in res1:
                    for k in res2:
                        self.helper(j,k,input[i])
                        res.append(self.helper(j,k,input[i]))
        return res

    def helper(self, m, n, op):
        if op == "+":
            return m + n
        if op == "-":
            return m - n
        else:
            return m * n
