class Solution:
    def similarPairs(self, words: List[str]) -> int:
        dicts=[]
        for word in words:
            dicts.append(set(word))
        count=0
        for i in range(len(dicts)):
            for j in range(i+1,len(dicts)):
                if dicts[i]==dicts[j]:
                    count+=1
        return count
