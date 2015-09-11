import sys

__author__ = 'Simon'
class Solution(object):
    def maxProfit(self, prices):
        # min = sys.maxint
        # max = -sys.maxint-1
        # buy = 0
        sell = 0
        # current_buy = 0
        if len(prices) < 2:
            return 0
        buy = prices[0]
        current_buy = sys.maxint
        for i in range(1, len(prices)):
            if prices[i] > buy and prices[i] > sell:
                    sell = prices[i]
            if prices[i] < buy and prices[i] < current_buy:
                current_buy = prices[i]
            if prices[i] - current_buy > sell - buy:
                sell = prices[i]
                buy = current_buy
                current_buy = sys.maxint
        if sell == 0:
            return 0
        else:
            return sell - buy

