__author__ = 'Simon'
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()
        self.DFS(candidates, target, 0, [], result)
        return result


    def DFS(self, candidates, target, amount, current, result):
        if amount == target:
            if current not in result:
                result.append(current[:])
        elif amount > target:
            return
        else:
            for i in range(len(candidates)):
                if amount + candidates[i] <= target:
                    self.DFS(candidates[i+1:], target, amount+candidates[i], current+[candidates[i]], result)
