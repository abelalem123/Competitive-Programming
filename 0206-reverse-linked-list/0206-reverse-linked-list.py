# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x,y=self.rec(head)
        return y
    def rec(self,head):
        if head==None:
            return None,None
        if head.next==None:
            return head,head
       
        p,h=self.rec(head.next)
        head.next=None
        p.next=head
        p=p.next
        
        return p,h