__author__ = 'Simon'
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # if headA == None or headB == None:
        #     return None
        #
        # Pre = None
        # while headA != None:
        #     Next = headA.next
        #     headA.next = Pre
        #     Pre = headA
        #     headA = Next
        #
        # Pre = None
        # while headB != None:
        #     Next = headB.next
        #     headB.next = Pre
        #     Pre = headB
        #     headB = Next
        #
        # Root = Pre
        # k = Pre
        #
        # if k.val != k.val:
        #     return None
        # else:
        #     while k.val == k.val:
        #         Result = headA
        #         headA = headA.next
        #         headB = headB.next
        #
        # Pre = None
        # Next = Root.next
        # Index = Root
        # while Next != None:
        #     Next = Root.next
        #     Root.next = Pre
        #     Pre = Root
        #     Root = Next
        #
        # while Root.val != Result.val:
        #     headA = headA.next
        #
        # return Result

        # stack1, stack2 = [], []
        # while headA:
        #     stack1.append(headA)
        #     headA = headA.next
        # while headB:
        #     stack2.append(headB)
        #     headB = headB.next
        # pre = None
        # while stack1 and stack2:
        #     if stack1[-1] is stack2.pop():
        #         pre = stack1.pop()
        #     else:
        #         return pre
        # return pre

        sizeA = 0
        sizeB = 0
        p1 = headA
        p2 = headB

        while p1:
            p1 = p1.next
            sizeA += 1

        while p2:
            p2 = p2.next
            sizeB += 1


        while sizeA != sizeB:
            if sizeA > sizeB:
                headA = headA.next
                sizeA -= 1
            elif sizeB > sizeA:
                headB = headB.next
                sizeB -= 1

        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        return None