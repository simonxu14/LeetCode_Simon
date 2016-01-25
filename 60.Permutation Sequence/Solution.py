class Solution(object):
    # def getPermutation(self, n, k):
    #     """
    #     :type n: int
    #     :type k: int
    #     :rtype: str
    #     """
    #     result = []
    #     num = []
    #     string = ""
    #     for i in range(1, n+1):
    #         num.append(i)
    #     self.DFS(num, string, result, k)
    #     # print len(result)
    #     return result.pop()
    #
    #
    # def DFS(self, num, string, result, k):
    #     if len(result) == k:
    #         return
    #     if len(num) == 0:
    #         result.append(string)
    #     else:
    #         for i in range(len(num)):
    #             self.DFS(num[:i] + num[i+1:], string + str(num[i]), result, k)


    def getPermutation(self, n, k):
        ll = [str(i) for i in range(1, n+1)]
        divisor = 1
        for i in range(1, n):
            divisor *= i
        answer = ""

        while k > 0 and k <= divisor * n:

            group_num = k / divisor
            # print group_num
            k %= divisor
            # print k

            if k > 0:
                # print "SSS"
                choose = ll.pop(group_num)
                answer += choose
            else:
                # print "AAA"
                choose = ll.pop(group_num - 1)
                answer += choose
                ll.reverse()

                to_add = "".join(ll)
                answer += to_add
                break

            divisor /= len(ll)

        return answer


if __name__ == '__main__':
    S = Solution()
    print S.getPermutation(3,4)

