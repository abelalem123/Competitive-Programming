class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        s1.sort()
        l = len(s1)
        for i in range(len(s2)-l+1):
            req = list(s2[i:i+l])
            req.sort()
            if req == s1:
                return (True)
        return False   