class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans=''
        for i in s:
            if i.isalpha():
                ans=ans+i
            elif i.isnumeric():
                ans=ans+i
        ans=ans.lower()
        print(ans)
        return ans==ans[::-1]
        
    #     class Solution:
    # def isPalindrome(self, s: str) -> bool:
    #     a = ""
    #     for x in [*s]:
    #         if x.isalpha(): a += x.lower()
    #         if x.isnumeric(): a += x
    #     return a == a[::-1]