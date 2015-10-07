__author__ = 'Simon'
# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#
#         """
#         :type nums1: List[int]
#         :type m: int
#         :type nums2: List[int]
#         :type n: int
#         :rtype: void Do not return anything, modify nums1 in-place instead.
#         """
#
#         if m == 0:
#             nums1[0:] = nums2[:n]
#             return
#         if n == 0:
#             nums1 = nums1[:m]
#             return
#
#         i = 0
#         j = 0
#
#         while i < m and j < n:
#             if nums1[i] <= nums2[j]:
#                 i += 1
#             else:
#                 nums1.insert(i, nums2[j])
#                 i += 1
#                 j += 1
#                 m += 1
#
#         if i >= m:
#             while j < n:
#                 nums1.insert(i, nums2[j])
#                 j += 1
#                 m += 1
#         nums1 = nums1[:m]
#         return

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[:] = nums1[:m] + nums2[:n]
        nums1.sort()