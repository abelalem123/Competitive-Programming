class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        map_values={}
        for s in strs:
            sortedString=''.join(sorted(s))
            if sortedString in map_values:
                map_values[sortedString].append(s)
            else:
                map_values[sortedString]=[s]
        
        return [x for x in map_values.values()]