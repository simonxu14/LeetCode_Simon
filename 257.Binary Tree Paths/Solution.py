__author__ = 'Simon'
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        list = []
        s = str(root.val)
        self.DFS(root, list, s)
        return list

    def DFS(self, root, list, s):
        if root.left == None and root.right == None:
            list.append(s)
        if root.left is not None:
            s = s + "->" + str(root.left.val)
            self.DFS(root.left, list, s)
            s = s[0:len(s) - len(str(root.left.val)) - 2]
        if root.right is not None:
            s = s + "->" + str(root.right.val)
            self.DFS(root.right, list, s)
            s = s[0:len(s) - len(str(root.right.val)) - 2]
        return