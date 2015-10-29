__author__ = 'Simon'
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        one = head
        two = head
        while two and two.next:
            one = one.next
            two = two.next.next
            if one is two:
                while head:
                    if head is one:
                        return head
                    head = head.next
                    one = one.next
        return None