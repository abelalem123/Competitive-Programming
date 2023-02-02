class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        words=[str(i) for i in nums]
        def compare(x,y):
            if x+y>y+x:
                return -1
            else:
                return 1
        words=sorted(words,key=cmp_to_key(compare))
        return str(int("".join(words)))  