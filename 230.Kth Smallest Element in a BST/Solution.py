__author__ = 'Simon'
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    global COUNT
    global RE
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        global COUNT
        global RE
        COUNT = 0
        RE = 0
        self.DFS(root, k)
        return RE

    def DFS(self, root, k):
        global COUNT
        global RE
        if root.left:
            self.DFS(root.left, k)
        COUNT = COUNT + 1
        if COUNT == k:
            RE = root.val
            return
        if root.right:
            self.DFS(root.right, k)