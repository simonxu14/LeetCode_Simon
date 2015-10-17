__author__ = 'Simon'
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # if len(nums) == 0:
        #     return None
        # root = TreeNode(nums[0])
        # list = []
        # list.append(root)
        #
        # i = 1
        # length = len(nums)
        # while i != length:
        #     Node1 = list[0]
        #     if i == length - 1:
        #         Node2 = TreeNode(nums[i])
        #         Node1.left = Node2
        #         i += 1
        #         break
        #     elif i <= length - 2:
        #         Node2 = TreeNode(nums[i])
        #         Node3 = TreeNode(nums[i+1])
        #         Node1.left = Node2
        #         list.append(Node2)
        #         Node1.right = Node3
        #         list.append(Node3)
        #         i += 2
        #     list.pop(0)
        # return root



        return self._toBST(nums, 0, len(nums))

    def _toBST(self, nums, l, r):
        if l == r:
            return None
        m = (l + r) >> 1
        root = TreeNode(nums[m])
        root.left = self._toBST(nums, l, m)
        root.right = self._toBST(nums, m + 1, r)
        return root