# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # arr=[]
        # while head:
        #     arr.append(head.val)
        #     head=head.next
        # l=0
        # r=len(arr)-1
        # m=0
        # print(arr)
        # while l<r:
        #     m=max(m,arr[l]+arr[r])
        #     l+=1
        #     r-=1
        # return m
        arr=[]
        l=0
        temp=head
        while temp:
            l+=1
            temp=temp.next
        temp=head
        count=0
        m=0
        while temp:
            if count<l/2:
                arr.append(temp.val)
            else:
                num=arr.pop(-1)
                m=max(m,num+temp.val)
            count+=1
            temp=temp.next
        return m
            