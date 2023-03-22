class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def search(x):
            l, r = 0, len(nums)           
            while l < r:
                mid = (l + r) // 2
                if nums[mid] < x:
                    l = mid+1
                else:
                    r = mid                    
            return l
        
        lower = search(target)
        higher = search(target+1)-1
        
        if lower <= higher:
            return [lower, higher]
                
        return [-1, -1]