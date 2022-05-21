# TC: O(N)  Here N = len  of the input string
# MC: O(1) 
class TreeNode:
    def __init__(self):
        self.word = ""
        self.next_nodes = [None] * 26
                
class Trie:

    def __init__(self):
        self.root = TreeNode()
        
        
    def insert(self, word: str) -> None:
        current_node = self.root
        
        for char in word:            
            pos = ord(char) - ord("a")

            if current_node.next_nodes[pos] is None:
                current_node.next_nodes[pos] = TreeNode()   
            current_node = current_node.next_nodes[pos]
        
        current_node.word =  word
              
    def find_suggestion(self, word) -> bool:
        words = []
    
        current_node = self.root
        
        for char in word:            
            pos = ord(char) - ord("a")

            if current_node.next_nodes[pos] is None:
                return words   
            current_node = current_node.next_nodes[pos]
            
        self.dfs(current_node, words) 
        
        return words
        
    def dfs(self, root,  words):
        
        if root is None or len(words)>=3:
            return 
        
        
        if len(root.word) >0:
            words.append(root.word)
            
        for idx in  range(26):
            if root.next_nodes[idx] is not None:
                self.dfs(root.next_nodes[idx], words)
            
    
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
         
        trie = Trie()
        
        for word in  products: 
            trie.insert(word)
            
        suggestions = []
        for idx in range(len(searchWord)):
            prefix_suggestion = trie.find_suggestion(searchWord[0:idx+1])        
            suggestions.append(prefix_suggestion)
               
        return suggestions
            