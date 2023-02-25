# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        while temp!=None:
           
            while temp.next and temp.val==temp.next.val:
                print(temp.val)
                temp.next=temp.next.next
            temp=temp.next
        return head
"""
1 2 2 2 2 3
"""