class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        """
        [
        [0,1,0],
        [1,2,1],
        [0,2,1]
        ]
        """
        ans=[0]*len(s)
        for i in shifts:
            if i[2]==0:
                ans[i[0]]-=1
                if i[1]<len(s)-1:
                    ans[i[1]+1]+=1
            else:
                ans[i[0]]+=1
                if i[1]<len(s)-1:
                    ans[i[1]+1]-=1
        sm=ans[0]
        for i in range(1,len(ans)):
            sm+=ans[i]
            ans[i]=sm
        for i in range(len(ans)):
            ans[i]=chr(((ord(s[i])-97+ans[i])%26)+97)
        return "".join(ans)
