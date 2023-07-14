class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent={i:i for i in range(len(stones))}
        
        size=[1]*len(stones)
        def find(x):
            if x==parent[x]:
                return x
            parent[x]=find(parent[x])
            return parent[x]

        def union(x,y):
            px=find(x)
            py=find(y)

            if px!=py:
                if size[px]>size[py]:
                    parent[py]=px
                    size[px]+=size[py]
                else:
                    parent[px]=py
                    size[py]+=size[px]
        for i in range(len(stones)):
            for j in range(i+1,len(stones)):
                xi,yi=stones[i]
                xj,yj=stones[j]

                if xi==xj or yi==yj:
                    union(i,j)
       
        return len(stones)-len(set(find(i) for i in range(len(stones))))
        
    
                                              