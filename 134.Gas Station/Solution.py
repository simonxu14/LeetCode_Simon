__author__ = 'Simon'
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        # sum = 0
        # result = bool()
        # for i in range(len(gas)):
        #     sum = sum + gas[i]
        #     sum = sum - cost[i]
        #     if sum < 0:
        #         result = 0
        #         return result
        # result = 1
        # return result
        diff = []
        sum = 0
        startnode = 0
        left = 0
        for i in range(len(gas)):
            diff.append(gas[i] - cost[i])
            sum += diff[i]
            left += diff[i]
            if sum < 0:
                startnode = i + 1
                sum = 0
        if left < 0:
            return -1
        else:
            return startnode