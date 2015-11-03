__author__ = 'Simon'
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        # stack = []
        # node = root
        # while node:
        #     stack.append(node)
        #     node = node.left
        # while stack:
        #     node = stack.pop()
        #     if node.right:
        #         node2 = node
        #         while node2.left != None:
        #             node2 = node2.left
        #
        #         node2.left = node.right
        #
        #         node3 = node.right
        #         while node3:
        #             stack.append(node3)
        #             node3 = node3.left
        # tmp = root
        # while tmp:
        #     print tmp.val
        #     tmp.right = tmp.left
        #     tmp = tmp.right

        if root is None:
            return
        right_stack = []
        while(root):
            if root.right:
                right_stack.append(root.right)
            if root.left:
                root.right = root.left
                root.left = None
                root = root.right
            elif right_stack:
                root.right = right_stack.pop()
                root = root.right
            else:
                return

















