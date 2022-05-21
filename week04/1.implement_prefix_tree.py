# TC: O(N)  Here N = len  of the input string
# MC: O(N) 

class TreeNode:
    def __init__(self):
        self.is_word = False
        self.next_nodes = [None] * 26
        
        
class Trie:

    def __init__(self):
        self.root = TreeNode()
        
# TC: O(N)  Here N = len  of the input string
# MC: O(N)        
    def insert(self, word: str) -> None:
        current_node = self.root
        
        for char in word:            
            pos = ord(char) - ord("a")

            if current_node.next_nodes[pos] is None:
                current_node.next_nodes[pos] = TreeNode()   
            current_node = current_node.next_nodes[pos]
        
        current_node.is_word = True

# TC: O(N)  Here N = len  of the input string
# MC: O(1)        
    def search(self, word: str, is_prefix = False) -> bool:
        current_node = self.root
        for char in word:            
            pos = ord(char) - ord("a")

            if current_node.next_nodes[pos] is None:
                return False
            current_node = current_node.next_nodes[pos]
        
        return current_node is not None and (current_node.is_word or is_prefix)
# TC: O(N)  Here N = len  of the input string
# MC: O(1)     
    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix, is_prefix = True)
    