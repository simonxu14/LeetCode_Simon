__author__ = 'Simon'
class Solution(object):
    # def nthUglyNumber(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     OPT = []
    #     OPT.append(1)
    #     L1 = []
    #     L2 = []
    #     L3 = []
    #     L1.append(2)
    #     L2.append(3)
    #     L3.append(5)
    #     i = 1
    #     number = 0
    #     while i < n:
    #         # if L1[len(L1)-1] == L2[len(L2)-1] and L1[len(L1)-1] == L3[len(L3)-1]:
    #         #     OPT.append(L1[len(L1)-1])
    #         #     L1.append(L1[len(L1)-1]+2)
    #         #     L2.append(L2[len(L2)-1]+3)
    #         #     L3.append(L3[len(L2)-1]+5)
    #         # elif L1[len(L1)-1] == L2[len(L2)-1] and L1[len(L1)-1] != L3[len(L3)-1]:
    #         #     OPT.append(L1[len(L1)-1])
    #         #     L1.append(L1[len(L1)-1]+2)
    #         #     L2.append(L2[len(L2)-1]+3)
    #         # elif L1[len(L1)-1] != L2[len(L2)-1] and L1[len(L1)-1] == L3[len(L3)-1]:
    #         #     OPT.append(L1[len(L1)-1])
    #         #     L1.append(L1[len(L1)-1]+2)
    #         #     L3.append(L3[len(L3)-1]+5)
    #         number = min(L1[len(L1)-1], L2[len(L2)-1], L3[len(L3)-1])
    #         OPT.append(number)
    #         if L1[len(L1)-1] == number and L2[len(L2)-1] == number and L3[len(L3)-1] == number:
    #             L1.append(L1[len(L1)-1]+2)
    #             L2.append(L2[len(L2)-1]+3)
    #             L3.append(L3[len(L3)-1]+5)
    #         elif L1[len(L1)-1] == number and L2[len(L2)-1] == number:
    #             L1.append(L1[len(L1)-1]+2)
    #             L2.append(L2[len(L2)-1]+3)
    #         elif L2[len(L2)-1] == number and L3[len(L3)-1] == number:
    #             L2.append(L2[len(L2)-1]+3)
    #             L3.append(L3[len(L3)-1]+5)
    #         elif L1[len(L1)-1] == number and L3[len(L3)-1] == number:
    #             L1.append(L1[len(L1)-1]+2)
    #             L3.append(L3[len(L3)-1]+5)
    #         elif L1[len(L1)-1] == number:
    #              L1.append(L1[len(L1)-1]+2)
    #         elif L2[len(L2)-1] == number:
    #              L2.append(L2[len(L2)-1]+3)
    #         elif L3[len(L3)-1] == number:
    #              L3.append(L3[len(L3)-1]+5)
    #         i += 1
    #     print OPT
    #     return OPT[n-1]


    def nthUglyNumber(self, n):
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        while n > 1:
            u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
            umin = min((u2, u3, u5))
            if umin == u2:
                i2 += 1
            if umin == u3:
                i3 += 1
            if umin == u5:
                i5 += 1
            ugly.append(umin)
            n -= 1
        print ugly
        return ugly[-1]

if __name__ == '__main__':
    S = Solution()
    print S.nthUglyNumber(11)