# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        temp_set={}
        
        while headA:
            temp_set[headA]=True
            headA=headA.next
        while headB:
            if headB in temp_set:
                return headB
            headB=headB.next