class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        cost=[[float('inf') if i!=j else 0 for j in range(n)] for i in range(n)]
        for u,v,d in edges:
            cost[u][v]=d
            cost[v][u]=d
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    cost[i][j]=min(cost[i][j],cost[i][via]+cost[via][j])
        d={}
        for i in range(n):
            c=0
            for j in range(n):
                if cost[i][j]<=distanceThreshold and i!=j:
                    c+=1
            d[i]=c
        m1=min(d.values())
        m2=0
        for k,v in d.items():
            if m1==v:
                m2=max(m2,k)
        return m2
        