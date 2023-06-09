class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ans=letters[0]
        for i in letters:
            if i!= target and i>target:
                ans=i
                break
        return ans