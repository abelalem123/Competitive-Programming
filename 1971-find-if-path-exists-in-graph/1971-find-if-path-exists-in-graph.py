class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent={i:i for i in range(n)}
        size=[1]*n
        def findd(x):
            if x==parent[x]:
                return x
            parent[x]=findd(parent[x])
            return parent[x]
        
        def union(x,y):
            px=findd(x)
            py=findd(y)
            
            if px!=py:
                if size[px]>size[py]:
                    parent[py]=px
                    size[px]+=size[py]
                else:
                    parent[px]=py
                    size[py]+=size[px]
                    
        def connected(x,y):
            return findd(x)==findd(y)
        
        for x,y in edges:
            union(x,y)
            
        return connected(source,destination)