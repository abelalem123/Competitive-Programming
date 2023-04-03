class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2=sorted([(v,i) for i,v in enumerate(nums2)])
        n=len(nums1)
        ans=[-1]*n
        l,r=0,n-1
        
        for i in range(n-1,-1,-1):
            if nums1[r]>nums2[i][0]:
                ans[nums2[i][1]]=nums1[r]
                r-=1
            else:
                ans[nums2[i][1]]=nums1[l]
                l+=1
        return ans
        