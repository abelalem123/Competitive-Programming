class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
    
    
    while node.next:
            node.val=node.next.val
            if node.next.next==None:
                node.next=None
                break
            node=node.next
            
