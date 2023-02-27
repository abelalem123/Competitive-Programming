class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        while temp!=None:
           
            while temp.next and temp.val==temp.next.val:
                print(temp.val)
                temp.next=temp.next.next
            temp=temp.next
        return head
