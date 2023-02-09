class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        indexs=[0]*26
        start=0
        end=0
        res=[]
        
        for i in range(len(s)):
            indexs[ord(s[i])-97]=i
        print(indexs)
        for i in range(len(s)):
            end=max(indexs[ord(s[i])-97],end)
            if i==end:
                res.append(i+1-start)
                start=i+1
        return res
            
            
            
            