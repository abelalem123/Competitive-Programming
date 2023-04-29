# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nums=[]
        while head:
            nums.append(head.val)
            head=head.next
        l=0
        r=len(nums)-1
        m=0
        while l<r:
            m=max(nums[l]+nums[r],m)
            r-=1
            l+=1
        return m
