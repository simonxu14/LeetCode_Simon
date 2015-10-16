__author__ = 'Simon'
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        list = []
        if root is None:
            return list
        self.preorder(root, list)
        return list

    def preorder(self, root, list):
        list.append(root.val)
        if root.left:
            self.preorder(root.left, list)
        if root.right:
            self.preorder(root.right, list)
