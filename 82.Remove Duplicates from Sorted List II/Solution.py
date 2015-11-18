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
        # if head is None:
        #     return head
        # if head.next is None:
        #     return head
        # node = head
        # pre = None
        # next = head.next
        # current = node.val
        # while next:
        #     if next.val == current:
        #         if node == head:
        #             head = next.next
        #             pre = None
        #             if head is None:
        #                 return head
        #             else:
        #                 next = head.next
        #         else:
        #             pre.next = next.next
        #             node = next.next
        #             if node is None:
        #                 return head
        #             else:
        #                 next = node.next
        #     else:
        #         pre = node
        #         node = next
        #         next = next.next
        #         current = node.val
        # return head
        #


        if head is None:
            return head
        if head.next is None:
            return head
        node = head
        pre = None
        while node.next:
            if node.next.val == node.val:
                while node.next.val == node.val:
                    node = node.next
                    if node.next is None:
                        break
                if node.next is None:
                    if pre == None:
                        return None
                    else:
                        pre.next = None
                        return head
                else:
                    if pre == None:
                        head = node.next
                        node = node.next
                    else:
                        pre.next = node.next
                        node = node.next
            else:
                pre = node
                node = node.next
        return head

