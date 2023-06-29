class Solution:
    def romanToInt(self, s: str) -> int:
        chars={}
        chars['I']=1
        chars['V']=5
        chars['X']=10
        chars['L']=50
        chars['C']=100
        chars['D']=500
        chars['M']=1000
        print(chars)
        ans=0
        i=0
        while i <len(s):
            if i+1<len(s):
                if chars[s[i+1]]>chars[s[i]]:
                    ans+=chars[s[i+1]]-chars[s[i]]
                    i+=2
                else:
                    ans+=chars[s[i]]
                    i+=1
            else:
                ans+=chars[s[i]]
                i+=1
        return ans