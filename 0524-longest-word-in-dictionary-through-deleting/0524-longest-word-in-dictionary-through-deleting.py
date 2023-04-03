class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort(key=lambda x: (-len(x), x))
        for word in d:
            i = 0
            for char in s:
                if i < len(word) and char == word[i]:
                    i += 1
                    if i == len(word):
                        break
            if i == len(word):
                return word
        return ""