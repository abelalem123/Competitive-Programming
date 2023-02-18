class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        l=[]
        for i in range(len(timePoints)):
            temp=timePoints[i]
            hr=temp[:2]
            mini=temp[3:]
            hr=int(hr)*60
            temp=hr+int(mini)
            l.append(temp)
        l.sort()
        out=1440
        for i in range(1,len(l)):
            if l[i]-l[i-1]<out:
                out=l[i]-l[i-1]
        x=l[-1]
        x=1440-x
        x=x+l[0]
        if x<out:
            return x
        return out