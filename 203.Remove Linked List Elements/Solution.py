__author__ = 'Simon'
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return head
        if head.next is None:
            if head.val == val:
                return None
            else:
                return head
        current = head
        pre = None
        while current:
            if current.val == val:
                if current == head:
                    head = head.next
                    current = current.next
                else:
                    pre.next = current.next
                    current = current.next
            else:
                current = current.next
                if pre == None:
                    pre = head
                else:
                    pre = pre.next
        return head