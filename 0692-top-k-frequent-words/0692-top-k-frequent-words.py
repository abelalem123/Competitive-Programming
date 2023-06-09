class Pair:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, p):
        return self.freq < p.freq or (self.freq == p.freq and self.word > p.word)
    
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d=defaultdict(int)
        for i in words:
            d[i]+=1
       
        h=[]
        for c,v in d.items():
            heapq.heappush(h, Pair(c,v))
            if len(h)>k:
                heapq.heappop(h)
            
        ans=[]
        for _ in range(k):
            ans.append( heapq.heappop(h))
        return reversed([i.word for i in ans])