__author__ = 'Simon'
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return head
        set = []
        set.append(head.val)
        current = head.next
        pre = head
        while current is not None:
            if current.val not in set:
                set.append(current.val)
                current = current.next
                pre = pre.next
            else:
                pre.next = current.next
                current = current.next
        return head
