class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(start: int, prev: int) -> bool:
            if start >= len(s):
                return True
            for i in range(start, len(s)):
                num = int(s[start:i+1])
                if (prev == -1 or prev-1 == num) and backtrack(i+1, num):
                    return True
            return False

        for i in range(1, len(s)):
            num = int(s[:i])
            if backtrack(i, num):
                return True
        return False