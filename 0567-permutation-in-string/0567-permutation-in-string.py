class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        s1.sort()
        l = len(s1)
        for i in range(len(s2)-l+1):
            sub = list(s2[i:i+l])
            sub.sort()
            if sub == s1:
                return True
        return False   