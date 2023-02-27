class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd=head 
        if head is None:
            return head    
        even = head.next
        evenhead = head.next
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next 
            even.next = even.next.next 
            even = even.next 
        odd.next = evenhead 
        return head
