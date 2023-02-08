class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        ans=[0]*2
        while(l<r):
            s=numbers[l]+numbers[r]
            if s==target:
                ans[0]=l+1
                ans[1]=r+1
                l+=1
                r-=1
            elif s>target:
                r-=1
            else:
                l+=1
        return ans