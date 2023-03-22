class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def bs(val,lst):
            l = 0
            r = len(lst)
            while l < r:
                
                mid = l + (r-l)//2
                
                
                if lst[mid] > val:
                    
                    r = mid 
                    
                else:
                    l = mid+1
                    
                    
            return len(lst) - l
        def f(word):

            bins = [0]*26

            smallest = "z"

            for ch in word:
                bins[ ord(ch) - 97  ] +=1

                if ch < smallest:
                    smallest = ch

            return bins[ord(smallest)-97]       
        wordsn = sorted([f(word) for word in words])
        ans = []   
        for q in queries:

            searchVal = f(q)


            ans.append(bs(searchVal,wordsn))

        return ans
        