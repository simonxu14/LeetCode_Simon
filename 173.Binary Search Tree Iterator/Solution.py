__author__ = 'Simon'
# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class BSTIterator(object):
#     def __init__(self, root):
#         """
#         :type root: TreeNode
#         """
#         self.root = root
#
#
#     def hasNext(self):
#         """
#         :rtype: bool
#         """
#         return self.root != None
#
#
#     def next(self):
#         """
#         :rtype: int
#         """
#         self.min = None
#         self.root = self.findSmallest(self.root)
#         return self.min
#
#     def findSmallest(self, root):
#         if root.left:
#             root.left = self.findSmallest(root.left)
#             return root
#         else:
#             self.min = root.val
#             return root.right


class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.nodes = []
        while root:
            self.nodes.append(root)
            root = root.left

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return len(self.nodes) > 0

    # @return an integer, the next smallest number
    def next(self):
        ret = self.nodes.pop()
        cur = ret.right
        while cur:
            self.nodes.append(cur)
            cur = cur.left

        return ret.val


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())