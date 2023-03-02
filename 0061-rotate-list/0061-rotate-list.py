# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow=head
        fast=head
        count=0
        temp=head
        if not head or not head.next:
            return head
        while temp:
            count+=1
            temp=temp.next
        print(count)
        if (k%count)==0:
            return head
        for i in range(k%count):
            fast=fast.next
        while fast.next:
            slow=slow.next
            fast=fast.next
        new_head=slow.next
        slow.next=None
        fast.next=head
        return new_head
            