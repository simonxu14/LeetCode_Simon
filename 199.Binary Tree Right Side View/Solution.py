__author__ = 'Simon'
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        stack = []
        stack.append(root)
        result = []
        result.append(root.val)
        layer = 1
        stack.append(root)
        current = []
        while stack:
            while stack:
                node = stack.pop(0)
                if node.left:
                    current.append(node.left)
                if node.right:
                    current.append(node.right)
            if current:
                result.append(current[-1].val)
            stack[:] = current[:]
            current[:] = []
        return result