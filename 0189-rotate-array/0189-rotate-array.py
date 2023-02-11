class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        def rotate(self,arr:List[int],l:int,r:int)->List[int]:
            
            while l<r:
                arr[l],arr[r]=arr[r],arr[l]
                l+=1
                r-=1
            return arr
        
        nums=rotate(self,nums,0,len(nums)-1)
        nums=rotate(self,nums,0,k-1)
        nums=rotate(self,nums,k,len(nums)-1)