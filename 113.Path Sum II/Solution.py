__author__ = 'Simon'
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        result = []
        self.DFS(root, sum, 0, [], result)
        return result

    def DFS(self, root, sum, amount, current, result):
        if amount + root.val == sum and root.left is None and root.right is None:
            result.append(current)
            return
        else:
            if root.left:
                self.DFS(root.left, sum, amount+root.val, current+[root], result)
            if root.right:
                self.DFS(root.left, sum, amount+root.val, current+[root], result)