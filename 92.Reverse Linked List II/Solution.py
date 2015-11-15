__author__ = 'Simon'
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head is None or m == n:
            return head
        index = 0
        node = head
        pre = None
        if m == 1:
            start = head
            while index == n:
                next = node.next
                node.next = pre
                node = next
                pre = node
                index += 1
            head = pre
            start.next = node
            return head
        else:
            index = 1
            while index == m:
                pre = node
                node = node.next
                index += 1
            node1 = pre
            start = node
            pre = None
            index -= 1
            while index == n:
                next = node.next
                node.next = pre
                node = next
                pre = node
                index += 1
            node1.next = pre
            start.next = node
            return head


