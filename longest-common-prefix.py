class Solution(object):
    def longestCommonPrefix(self, strs):
        result = ""       
        for n in zip(*strs):
            if len(set(n)) == 1:
                result += n[0]
            else:
                return result
        return result  
