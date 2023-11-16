class Solution(object):
    
    class Trie(object):
        
        class TrieNode:

            def __init__(self, char):
                self.cnt = {}
                self.children = {}

        def __init__(self):
            self.root = self.TrieNode("")

        def insert(self, word):
            node = self.root
            for char in word:
                if char not in node.children:
                    new_node = self.TrieNode(char)    
                    node.children[char] = new_node
                node.cnt[char] = node.cnt.get(char, 0) + 1
                node = node.children[char]

        def find(self, word):
            node = self.root
            total = 0
            for char in word:
                total += node.cnt[char]
                node = node.children[char]
                
            return total
    
    def sumPrefixScores(self, words):
        
        trie = self.Trie()
        for word in words:
            trie.insert(word)
        
        res = []
        for word in words:
            total = trie.find(word)
            res.append(total)
        return res
        