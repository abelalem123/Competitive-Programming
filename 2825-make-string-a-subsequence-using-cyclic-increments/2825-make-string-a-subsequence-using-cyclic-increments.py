class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:

        
        
        l=0
        r=0
        if len(str1)<len(str2):
            return False

        while r<len(str2):
            if l<len(str1):
                x=(ord(str2[r])-96)%26-(ord(str1[l])-96)%26
                y=(ord(str2[r])-96)%26-(ord(str1[l])-95)%26
                print()
                if  x==0 or y==0:
                    print('hey')
                    r+=1
                    l+=1
                else:
                    if l<len(str1)-1:
                        l+=1
                    else:
                        return False
            else:
                return False
        return True
