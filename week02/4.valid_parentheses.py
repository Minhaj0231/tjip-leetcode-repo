#TC: O(N) here n is the  len of the input string
# MC: O(N) 
class Solution:
    def isValid(self, s: str) -> bool:
        
        brackets_dict  = {
            ")":"(",
            "}" :"{",
            "]" : "[" 
        }
        stack = []
        valid = True
        for idx in range (0, len(s)):
           
            if s[idx]  in brackets_dict:
                if len(stack) <= 0 or stack[len(stack)-1] != brackets_dict[s[idx]]:
                    valid = False
                    break
                else:
                    stack.pop()
                    
            else: 
                stack.append(s[idx])
                
        if len(stack)>0 or not valid:
            return False
        
        return True