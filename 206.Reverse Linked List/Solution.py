__author__ = 'Simon'
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Your runtime beats 98.99% of python submissions.
        # Your runtime beats 0.38% of python submissions.
        # set = []
        # current = head
        #
        # while current != None:
        #     set.append(current.val)
        #     current = current.next
        # result = head
        # while len(set) != 0:
        #     head.val = set[len(set)-1]
        #     set.pop()
        #     head = head.next
        # return result


        # Your runtime beats 94.18% of python submissions.
        prev = None
        current = head
        next = None

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next

        return prev