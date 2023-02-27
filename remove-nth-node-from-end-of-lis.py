class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast=head
        slow=head
       
        for i in range(n):
            fast=fast.next 
        if fast==None:
            return head.next
        while fast.next!=None:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return head
