class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle = [i for i in range(1, n+1)]
        lastIndex = 0
        while len(circle) > 1:
            lastIndex = (lastIndex + k - 1) % len(circle)
            del circle[lastIndex]
        return circle[0]
