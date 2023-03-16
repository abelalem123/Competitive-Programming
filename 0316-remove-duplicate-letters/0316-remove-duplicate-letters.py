class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s) # initialize frequency hashmap
        st = []
        taken = set()
        for char in s:
            if char not in taken:
                while st and st[-1] > char and count[st[-1]] > 0:
                    taken.remove(st.pop())
                st.append(char)
                taken.add(char)
            count[char] -= 1 
        return ''.join(st)