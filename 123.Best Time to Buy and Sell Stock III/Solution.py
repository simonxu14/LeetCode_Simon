__author__ = 'Simon'
class Solution(object):
    def maxProfit(self, prices):
    #     """
    #     :type prices: List[int]
    #     :rtype: int
    #     """
    #     if len(prices) <=2:
    #         return 0
    #     result = 0
    #     current = 0
    #     for i in range(1, len(prices)):
    #         current = self.computeMax(prices[:i]) + self.computeMax(prices[i:])
    #         if current > result:
    #             result = current
    #     return result
    #
    # def computeMax(self, prices):
    #     if len(prices) <= 1:
    #         return 0
    #     OPT = [0 for i in range(len(prices)+1)]
    #     OPT[0] = 0
    #     OPT[1] = 0
    #     for i in range(2, len(prices)+1):
    #         OPT[i] = max(0, OPT[i-1] - prices[i-2] + prices[i-1])
    #     return max(OPT)











        # if len(prices) <= 2:
        #     return 0
        # OPT = [0 for i in range(len(prices)+1)]
        # OPT[0] = 0
        # OPT[1] = 0
        # for i in range(2, len(prices)+1):
        #     OPT[i] = max(0, OPT[i-1] - prices[i-2] + prices[i-1])
        # # print OPT
        #
        # prices2 = []
        # for i in range(len(prices)):
        #     prices2.append(prices[len(prices)-1-i])
        #
        # OPT2 = [0 for i in range(len(prices2)+1)]
        # OPT2[0] = 0
        # OPT2[1] = 0
        # for i in range(2, len(prices2)+1):
        #     OPT2[i] = min(0, OPT2[i-1] - prices2[i-2] + prices2[i-1])
        # # print OPT2
        # result = 0
        # current = 0
        # for i in range(2, len(prices)):
        #     current = max(OPT[0:i+1]) + min(OPT2[0:len(prices)-i+1])*(-1)
        #     if current > result:
        #         result = current
        # return result











        # if len(prices) <= 2:
        #     return 0
        # OPT = [0 for i in range(len(prices)+1)]
        # OPT[0] = 0
        # OPT[1] = 0
        # for i in range(2, len(prices)+1):
        #     OPT[i] = max(0, OPT[i-1] - prices[i-2] + prices[i-1])
        #
        # result = 0
        # current = 0
        # for i in range(2, len(prices)-1):
        #     current = max(OPT[:i+1]) + max(OPT[i+1:]) - min(OPT[i+1:])
        #     if current > result:
        #         result = current
        # return result






        # profit = [0]*len(prices)
        # low, high = float('inf'), float('-inf')
        # max_profit = res = 0
        # for n, p in enumerate(prices):
        #     low = min(p, low)
        #     max_profit = max(max_profit, p-low)
        #     profit[n] = max_profit
        # max_profit = 0
        # for n, p in reversed(list(enumerate(prices))):
        #     high = max(p, high)
        #     max_profit = max(max_profit, high-p)
        #     res = max(res, max_profit+profit[n])
        # return res




        if len(prices) < 2:
            return 0
        OPT = [0 for i in range(len(prices))]
        OPT[0] = 0
        highPrice = prices[0]
        lowPrice = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > highPrice:
                highPrice = prices[i]
                OPT[i] = highPrice - lowPrice
            elif prices[i] < lowPrice:
                OPT[i] = OPT[i-1]
                lowPrice = prices[i]
                highPrice = prices[i]
            else:
                OPT[i] = OPT[i-1]
        print OPT



        prices2 = []
        for i in range(len(prices)):
            prices2.append(prices[len(prices)-1-i])
        # print prices2

        result = 0

        OPT2 = [0 for i in range(len(prices2))]
        OPT2[0] = 0

        highPrice = prices2[0]
        lowPrice = prices2[0]

        for i in range(1, len(prices2)):
            if prices2[i] < lowPrice:
                lowPrice = prices2[i]
                OPT2[i] = highPrice - lowPrice
            elif prices2[i] > highPrice:
                OPT2[i] = OPT2[i-1]
                highPrice = prices2[i]
                lowPrice = prices2[i]
            else:
                OPT2[i] = OPT2[i-1]
            if result < OPT2[i] + OPT[len(prices)-i-1]:
                result = OPT2[i] + OPT[len(prices)-i-1]
        print OPT2
        return result






if __name__ == '__main__':
    S = Solution()
    prices = [1,2,3,4,1,2,3,4,1,2]
    print S.maxProfit(prices)