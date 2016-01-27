# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        h = self.height(root)
        nodes = 0
        while root:
            if self.height(root.right) == h - 1:
                nodes += 2 ** h
                root = root.right
            else:
                nodes += 2 ** (h-1)
                root = root.left
            h -= 1
        return nodes


    def height(self, root):
        if root is None:
            return -1
        else:
            return self.height(root.left) + 1


        # if root is None:
        #     return 0
        # num = 0
        # stack = []
        # stack.append(root)
        # while stack:
        #     node = stack.pop()
        #     num += 1
        #     if node.left is not None:
        #         stack.append(node.left)
        #     if node.right is not None:
        #         stack.append(node.right)
        # return num