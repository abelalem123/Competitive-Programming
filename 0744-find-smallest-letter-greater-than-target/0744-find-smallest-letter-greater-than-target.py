class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ans=letters[0]
        x=bisect_right(letters,target)
        if 0<=x<len(letters):
            ans=letters[x]
        return ans