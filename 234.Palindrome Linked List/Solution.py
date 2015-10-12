__author__ = 'Simon'
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True
        if head.next is None:
            return True

        length = 0
        k = ListNode(None)
        k = head
        while k:
            k = k.next
            length += 1

        number = length / 2
        index = 0
        pre = ListNode(None)
        m = ListNode(None)
        next = ListNode(None)
        m = head
        next = head

        while index != number:
            next = m.next
            next.next = m
            m.next = pre
            pre = m
            m = next
            index += 1

        i = ListNode(None)
        j = ListNode(None)

        if length % 2 == 0:
            i = pre
            j = m
        else:
            i = pre
            j = m.next

        while i:
            if i.val != j.val:
                return False
            i = i.next
            j = j.next
        return True
