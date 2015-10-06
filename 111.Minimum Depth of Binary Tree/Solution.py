import sys

__author__ = 'Simon'
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        list = []
        long = 0
        self.DFS(root, long, list)
        result = sys.maxint
        for i in list:
            if i < result:
                result = i
        return result

    def DFS(self, root, long, list):
        if root.left is None and root.right is None:
            list.append(long + 1)
        if root.left:
            long += 1
            self.DFS(root.left, long, list)
            long -= 1
        if root.right:
            long += 1
            self.DFS(root.right, long, list)
            long -= 1
        return