class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l=0
        r=len(people)-1
        count=0
        while l<=r:
            s=people[l]+people[r]
            if s<=limit:    
                l+=1
            r-=1
            count+=1
        return count