class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i,j=m-1,n-1
        k=m+n-1
        while j>-1 or i>-1:
            if j<0 or i>-1 and nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                i-=1
                k-=1
            else:
                nums1[k]=nums2[j]
                j-=1
                k-=1
        
        
        
        
        
        
        
        
        
        
#         i, j = m-1, n-1
#         for right in range(m+n-1, -1, -1):
#             if j < 0:
#                 break
#             if i >= 0 and nums1[i] > nums2[j]:
#                 nums1[right] = nums1[i]
#                 i -= 1
#             else:
#                 nums1[right] = nums2[j]
#                 j -= 1
        