class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0]))
        i=0
        n=len(intervals)
        while i<n-1:
            if intervals[i][1]>=intervals[i+1][0] and intervals[i][0]<=intervals[i+1][1]:
                num1= min(intervals[i][0],intervals[i+1][0])
                num2= max(intervals[i][1],intervals[i+1][1])
                intervals.pop(i)
                intervals.pop(i)
                intervals.insert(i,[num1,num2])
                n=n-1
            else:
                i=i+1
        return intervals