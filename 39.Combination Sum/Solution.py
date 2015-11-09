__author__ = 'Simon'
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()
        self.DFS(candidates, target, [], result)
        return result

    def DFS(self, candidates, target, current, result):
        for i in range(len(candidates)):
            if candidates[i] > target:
                return
            elif candidates[i] == target:
                result.append(current+[candidates[i]])
                return
            else:
                print current+[candidates[i]]
                self.DFS(candidates[i:], target-candidates[i], current+[candidates[i]], result)
