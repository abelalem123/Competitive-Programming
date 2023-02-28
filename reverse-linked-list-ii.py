class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        # Move to the node before the start node
        for i in range(left - 1):
            prev = prev.next
        start = prev.next
        end = start.next
        # Reverse the nodes
        for i in range(right - left):
            start.next = end.next
            end.next = prev.next
            prev.next = end
            end = start.next
        return dummy.next
