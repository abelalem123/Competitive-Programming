# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp=ListNode(0)
        self.rec(temp,head,val)
        return temp.next
    def rec(self,temp,head,val):
        if head==None:
            return None
        if head.val!=val:
            temp.next=ListNode(head.val)
            temp=temp.next
        
        self.rec(temp,head.next,val)
        return head