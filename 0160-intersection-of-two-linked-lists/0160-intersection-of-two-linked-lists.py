# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
       

    # def getIntersectionNode(headA, headB):
        lenA = 0
        lenB = 0
        pA = headA
        pB = headB
        while pA:
            lenA += 1
            pA = pA.next
        while pB:
            lenB += 1
            pB = pB.next
        pA = headA
        pB = headB
        if lenA > lenB:
            for i in range(lenA - lenB):
                pA = pA.next
        else:
            for i in range(lenB - lenA):
                pB = pB.next
        while pA and pB:
            if pA == pB:
                return pA
            pA = pA.next
            pB = pB.next
        return None