
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        node=ListNode(0)
        temp=head
        temp_node=node
        while temp:
            temp_node.next=ListNode(temp.val)
            temp_node=temp_node.next
            temp=temp.next
        previous_node=None
        current_node=node.next
        
        while current_node:
            next_node=current_node.next
            current_node.next=previous_node
            previous_node=current_node
            current_node=next_node
       
        while head:
            if previous_node.val!=head.val:
                return False
            previous_node=previous_node.next
            head=head.next
        return True
            
