__author__ = 'Simon'
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        list = []
        self.DFS(root, root.val, list)
        if sum in list:
            return True
        else:
            return False

    def DFS(self, root, num, list):
        if root.left == None and root.right == None:
            list.append(num)
            return
        if root.left:
            num = num + root.left.val
            self.DFS(root.left, num, list)
            num = num - root.left.val
        if root.right:
            num = num + root.right.val
            self.DFS(root.right, num, list)
            num = num - root.right.val
        return