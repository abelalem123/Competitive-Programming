class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        sett=set()
        m=0
        while r<len(s):
            while s[r] in sett:
                sett.remove(s[l])
                l+=1
            sett.add(s[r])
            m=max(m,r-l+1)
            r+=1
        return m