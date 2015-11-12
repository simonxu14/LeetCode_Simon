__author__ = 'Simon'
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
    #     if q == p:
    #         return p
    #     return self.check(root, p, q)
    #
    #
    # def check_node(self, root, node):
    #     if root is None:
    #         return False
    #     if root == node:
    #         return True
    #     else:
    #         return self.check_node(root.left, node) or self.check_node(root.right, node)
    #
    # def check(self, root, p, q):
    #     if root == p:
    #         # if root.left:
    #         #     if self.check_node(root.left, q) == True:
    #         #         return p
    #         # if root.right:
    #         #     if self.check_node(root.right, q) == True:
    #         #         return p
    #         if self.check_node(root.left, q) or self.check_node(root.right, q) == True:
    #             return p
    #     elif root == q:
    #         # if root.left:
    #         #     if self.check_node(root.left, p) == True:
    #         #         return p
    #         # if root.right:
    #         #     if self.check_node(root.right, p) == True:
    #         #         return q
    #         if self.check_node(root.left, p) or self.check_node(root.right, p) == True:
    #             return q
    #     else:
    #         if (self.check_node(root.left, p) and self.check_node(root.right, q)) or (self.check_node(root.left, q) and self.check_node(root.right, p)):
    #             return root
    #         if self.check_node(root.left, p) and self.check_node(root.left, q):
    #             return self.check(root.left, p, q)
    #         if self.check_node(root.right, p) and self.check_node(root.right, q):
    #             return self.check(root.right, p, q)



        if not root:
            return
        if self.isDescendantOf(p, q):
            return p
        if self.isDescendantOf(q, p):
            return q

        if self.isDescendantOf(root.left, p) and self.isDescendantOf(root.right, q) or self.isDescendantOf(root.left, q) and self.isDescendantOf(root.right, p):
            return root
        else:
            return self.lowestCommonAncestor(root.left, p, q) or self.lowestCommonAncestor(root.right, p, q)




    def isDescendantOf(self, x, y):
        """
        Check if y is a descendant of x
        """
        if x is None:
            return False
        if x == y:
            return True
        else:
            return self.isDescendantOf(x.right, y) or self.isDescendantOf(x.left, y)