
# TC: O(N)  Here N = len  of the nodes in the tree
# MC: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        self.pattern_dict = {}
        self.findPattern(root)
        
        duplicates = []
        for pattern in self.pattern_dict:
            pattern_list = self.pattern_dict[pattern]
            if pattern_list[1] > 1:
                duplicates.append(pattern_list[0])
    
        return duplicates
    
    def  findPattern(self, root):
        if  root == None:
            return root
        
        left_pattern = self.findPattern(root.left)
        right_pattern = self.findPattern(root.right)
        pattern = (root.val, left_pattern, right_pattern)
        
        if pattern in self.pattern_dict:
            pattern_list =  self.pattern_dict[pattern] 
            pattern_list[1] +=1
            self.pattern_dict[pattern] =  pattern_list 
            
        else:
            self.pattern_dict[pattern] = [root, 1]
            
    
        return pattern