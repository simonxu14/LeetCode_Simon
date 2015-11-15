__author__ = 'Simon'
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        stack1 = []
        stack2 = []
        result = []
        current = []
        stack1.append(root)
        current.append(root.val)
        result.append(current[:])
        while stack1:
            while stack1:
                node = stack1.pop(0)
                if node.left:
                    stack2.append(node.left)
                if node.right:
                    stack2.append(node.right)
            if len(stack2) != 0:
                current = []
                for i in range(len(stack2)):
                    current.append(stack2[i].val)
                result.append(current[:])
            stack1 = stack2
            stack2 = []
        for i in range(len(result)):
            if i%2 == 1:
                result[i].reverse()
        return result
