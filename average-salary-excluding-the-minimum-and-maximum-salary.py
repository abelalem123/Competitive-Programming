class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        sum=0
        for i in range(1,len(salary)-1):
            sum+=salary[i]
        sum=sum/(len(salary)-2)
        return sum
