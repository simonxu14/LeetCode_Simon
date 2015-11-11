__author__ = 'Simon'
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        current = head
        while current.next:
            pre = head
            if current.next.val >= current.val:
                current = current.next
            else:
                if current.next.val < head.val:
                    node = current.next
                    current.next = node.next
                    node.next = head
                    head = node
                else:
                    while pre.next.val < current.next.val:
                        pre = pre.next
                    node = current.next
                    current.next = node.next
                    node.next = pre.next
                    pre.next = node
        return head