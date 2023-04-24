# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
    # def swapPairs(head):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        while curr and curr.next:
            next_node = curr.next
            curr.next = next_node.next
            next_node.next = curr
            prev.next = next_node
            prev = curr
            curr = curr.next
        return dummy.next