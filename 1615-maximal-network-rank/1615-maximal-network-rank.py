class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graphs=defaultdict(set)
        for u,v in roads:
            graphs[u].add(v)
            graphs[v].add(u)
            
        res=0
        for c1,c2 in itertools.combinations(graphs.keys(),2):
            con=1 if c1 in graphs[c2] else 0
            
            city1=len(graphs[c1])
            city2=len(graphs[c2])
            
            res=max(res,city1+city2-con)
        return res