class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        max_len=0
        while l<r:
            length=min(height[l],height[r])
            dist=r-l
            max_len=max(max_len,length*dist)
            if height[l]>=height[r]:
                r-=1
            elif height[l]<height[r]:
                l+=1
            
        return max_len
