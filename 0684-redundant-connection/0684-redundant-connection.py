class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)+1
        parent={i:i for i in range(1,n)}
        size=[1]*n
        
        def find(x):
            if x==parent[x]:
                return x
            parent[x]=find(parent[x])
            return parent[x]
        
        def union(x,y):
            px=find(x)
            py=find(y)
            
            if px!=py:
                if size[px]>py:
                    parent[py]=px
                    size[px]+=size[py]
                else:
                    parent[px]=py
                    size[py]+=size[px]
        for x,y in edges:
            if find(x)==find(y):
                return [x,y]
            union(x,y)