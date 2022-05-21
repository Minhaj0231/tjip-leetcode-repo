# TC: O(N)  Here N = len  of the input string
# MC: O(N)   
class TreeNode:
    def __init__(self):
        self.is_word = False
        self.next_nodes = [None] * 26
        
        
class Trie:

    def __init__(self, size):
        self.root = TreeNode()
        self.mem = [None]* (size)
        
        
    def insert(self, word: str) -> None:
        current_node = self.root
        
        for char in word:            
            pos = ord(char) - ord("a")

            if current_node.next_nodes[pos] is None:
                current_node.next_nodes[pos] = TreeNode()   
            current_node = current_node.next_nodes[pos]
        
        current_node.is_word = True

    def break_word(self, word: str, word_pos) -> bool:
        if word_pos >= len(word):
            return True
        
        canBreak = False
        current_node = self.root
        for idx in range(word_pos, len(word)): 
            pos = ord(word[idx]) - ord("a")
            if current_node.next_nodes[pos] is None:
                return False
            if current_node.next_nodes[pos].is_word and self.mem[idx] != False:
                canBreak = self.break_word(word, idx+1)
                
                if canBreak:
                    return True
                self.mem[idx] = canBreak
                
            current_node = current_node.next_nodes[pos]
        return canBreak
            
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
       
        trie = Trie(len(s))
        for word in wordDict:
            trie.insert(word)
            
        result = trie.break_word(s, 0)
        return result