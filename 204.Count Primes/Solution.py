import itertools

__author__ = 'Simon'
class Solution(object):
    # def countPrimes(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     list = []
    #     for i in range(2,n+1):
    #         list.append(i)
    #     # print list
    #     m = 0
    #     while m < len(list):
    #         if list[m] == 2 or list[m] == 3 or list[m] == 5 or list[m] == 7:
    #             m += 1
    #         elif list[m] % 2 == 0 or list[m] % 3 == 0 or list[m] % 5 == 0 or list[m] % 7 == 0:
    #             # print "AAA"
    #             list.pop(m)
    #             m += 1
    #     print list
    #     k = 0
    #     result = []
    #     prime = True
    #     n = 0
    #     for k in range(len(list)):
    #         n = k/2
    #         for p in range(n):
    #             if list[k] % list[p] == 0:
    #                 prime = False
    #         if prime == True:
    #             result.append(list[k])
    #     return len(result)
    #

    def countPrimes(self, n):
        if n <= 2:
            return 0
        res = [True] * n
        res[0] = res[1] = False
        for i in xrange(2, n):
            if res[i] == True:
                for j in xrange(2, (n-1)//i + 1):
                    res[i*j] = False
        return sum(res)

if __name__ == '__main__':
    S = Solution()
    print S.countPrimes(5)
