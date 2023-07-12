class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent={}
        size={}
        for i in equations:
            parent[i[0]]=i[0]
            size[i[0]]=1
            parent[i[3]]=i[3]
            size[i[3]]=1
        def find(x):
            if x==parent[x]:
                return x
            parent[x]=find(parent[x])
            return parent[x]
        
        def union(x,y,eq):
            px=find(x)
            py=find(y)
            
            if px!=py:
                if eq=='=':
                    if size[px]>size[py]:
                        parent[py]=px
                        size[px]+=size[py]
                    else:
                        parent[px]=py
                        size[py]+=size[px]
        
        for q in equations:
            if q[1]=='=':
                union(q[0],q[3],q[1])
        for q in equations:
            if q[1]=='!':
                if find(q[0])==find(q[3]):
                    return False
            
        return True
            