class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        n = len(adjacentPairs) + 1
        adj = collections.defaultdict(list)

        for n1, n2 in adjacentPairs:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        node = next(filter(lambda x: len(adj[x])==1,adj.keys()))
        ret = []
        prev = None

        while True:
            ret.append(node)
            for a in adj[node]:
                if a != prev:
                    prev = node
                    node = a
                    break
            else:
                break
        
        return ret
