# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small=ListNode(0)
        small_head=small
        large=ListNode(0)
        large_head=large
        temp=head
        while temp:
            if temp.val<x:
                small.next=temp
                small=small.next
            else:
                large.next=temp
                large=large.next
            temp=temp.next
        large.next=None
        small.next=large_head.next
        
        return small_head.next