import heapq

__author__ = 'Simon'
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # heap = nums[:k]
        # heapq.heapify(heap)
        # for i in nums[k:]:
        #     if i > heap[0]:
        #         heapq.heapreplace(heap, i)
        # return heap[0]


        heap = nums[:k]
        heapq.heapify(heap)
        for i in nums[k:]:
            if i > heap[0]:
                heapq.heappop(0)
                heapq.heappush(heap, i)
        return heap[0]