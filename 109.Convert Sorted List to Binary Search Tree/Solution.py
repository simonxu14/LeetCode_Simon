__author__ = 'Simon'
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        size = len(nums)
        if size == 0:
            return None
        return self.buildBST(0, size-1, nums)

    def buildBST(self, begin, end, nums):
        if begin > end:
            return None
        if begin == end:
            return TreeNode(nums[begin])
        mid = (begin+end)/2
        root = TreeNode(nums[mid])
        root.left = self.buildBST(begin, mid-1, nums)
        root.right = self.buildBST(mid+1, end, nums)
        return root