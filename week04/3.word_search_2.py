# TC: O(4* 3^(word_length))  
# MC: O(N)  Here N = len  of the input string array 
class TreeNode:
    def __init__(self):
        self.word = ""
        self.next_nodes = [None] * 26
        self.direction = [-1,0,1,0,-1]
                
class Trie:

    def __init__(self):
        self.root = TreeNode()
        self.direction = [-1,0,1,0,-1]
        
    def insert(self, word: str) -> None:
        current_node = self.root
        
        for char in word:            
            pos = ord(char) - ord("a")

            if current_node.next_nodes[pos] is None:
                current_node.next_nodes[pos] = TreeNode()   
            current_node = current_node.next_nodes[pos]
        
        current_node.word =  word
              
    def search(self,i,j,board, root,words_on_board):
        char = board[i][j];
        
        pos = ord(char) - ord("a")
        
        if root and len(root.word) >0:
            words_on_board.append(root.word)
            root.word = ""
        
        if root and root.next_nodes[pos] == None:
            return 
            
        root = root.next_nodes[pos]
        board[i][j] = "#"
        
        
        for idx in range(4):
            x = i + self.direction[idx]
            y = j + self.direction[idx+1]
            
            if (x<0 or y<0 or x>= len(board) or y >= len(board[0]) or board[x][y] == "#"  ):
                continue
            self.search(x,y, board,root,words_on_board)
                 
        board[i][j] = char
        
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        trie = Trie()
        for word in words:
            trie.insert(word)
            
        words_on_board = []
        
        for i in range(len(board)):
            for j in range(len(board)):
                trie.search(i,j,board, trie.root, words_on_board)
                      
        return words_on_board
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        