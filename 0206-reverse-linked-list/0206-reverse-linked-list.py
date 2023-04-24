# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x,y=self.reverse(head)
        return x

    def reverse(self, head):
        if head == None or head.next == None:
            return head, head
        last,node = self.reverse(head.next)
        head.next=None
        node.next=head
        node=node.next
        return last,node