class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        [1,2,3,4,5,6,7,8,9,10]
        """
        left=max(weights)
        right=sum(weights)
        
        while left<right:
            mid=(left+right)//2
            
            count=1
            total=0
            
            for i in weights:
                if i+total>mid:
                    count+=1
                    total=i
                else:
                    total+=i
            
            if count>days:
                left=mid+1
            else:
                right=mid
        return left