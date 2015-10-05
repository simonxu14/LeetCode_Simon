__author__ = 'Simon'
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        result = []
        layer = []
        current = []
        current_number =[]

        current.append(root)
        current_number.append(root.val)
        result.append(current_number)
        print result

        layer.append(root)
        current = []
        current_number = []

        while layer:
            for node in layer:
                if node.left:
                    current.append(node.left)
                    current_number.append(node.left.val)
                if node.right:
                    current.append(node.right)
                    current_number.append(node.right.val)
            if current:
                result.insert(0, current_number)
            layer = current
            current = []
            current_number = []

        return result
