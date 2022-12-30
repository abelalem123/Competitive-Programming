class Solution:
    def freqAlphabets(self, s: str) -> str:
        length=-len(s)-1
        i=-1
        alphabet=[]
        ans=''
        while i>length:
            if s[i]=="#":
                sg=''
                i-=1
                sg+=str(s[i])
                i-=1
                sg+=str(s[i])
                alphabet.append(sg[::-1])
                i-=1
            else:
                alphabet.append(str(s[i]))
                i-=1  
        alphabet.reverse()
        for letter in alphabet:
            ans+=chr(int(letter)+96)
        return ans
