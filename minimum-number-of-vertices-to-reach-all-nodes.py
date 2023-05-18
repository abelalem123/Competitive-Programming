class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        outgoing={i for i,j in edges}
        incoming={j for i,j in edges}
        return outgoing-incoming
