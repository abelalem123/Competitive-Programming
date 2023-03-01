# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
            
        start=ListNode(0)
        start.next=head
        c=start
        while c.next and c.next.next:
            first=c.next
            second=c.next.next
            first.next=second.next
            second.next=first
            c.next=second
            c=c.next.next
         
        return start.next