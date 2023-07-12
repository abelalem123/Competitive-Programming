class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent={}
        for i in range(len(s1)):
            parent[s1[i]]=s1[i]
            parent[s2[i]]=s2[i]
        def find(x):
            if x==parent[x]:
                return x
            parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            px=find(x)
            py=find(y)
            
            if px!=py:
                if px<py:
                    parent[py]=px
                else:
                    parent[px]=py
        for i in range(len(s1)):
            union(s1[i],s2[i])
        
        s=''
        for i in baseStr:
            if i in parent:

                s+=find(i)
            else:
                s+=i
        return s