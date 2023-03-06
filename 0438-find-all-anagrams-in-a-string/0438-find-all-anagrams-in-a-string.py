class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k=len(p)
        pov=sorted(list(p))
        s=list(s)
        ans=[]
        l=0
        r=k
        while r<=len(s):
            sub=sorted(s[l:r])
            if pov==sub:
                ans.append(l)
            r+=1
            l+=1
        return ans
            