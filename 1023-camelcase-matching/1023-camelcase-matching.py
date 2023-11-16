class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def match(s):
            t,j,m,n=0,0,len(pattern),len(s)
            for i in range(n):
                if j==m:
                    t=i
                    break
                if pattern[j]==s[i]:
                    j+=1
                else:
                    if s[i].isupper():
                        return False
            if t!=0:
                for i in range(t+1,n):
                    if s[i].isupper():
                        return False
            return j==m
        a=[]
        for i in queries:
            a.append(match(i))
        return a