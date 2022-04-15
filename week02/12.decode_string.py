# TC: O(N)
# MC: O(N) 
class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        
        current_slice = ""
        
        num = 0
        
        for  idx in range(0, len(s)):
            if  s[idx].isdigit():
                num = num*10 + int(s[idx])
                
            elif s[idx] == "[":
                stack.append ([current_slice,num])
                current_slice = ""
                num = 0
            elif s[idx] == "]":
                prev_slice, prev_num = stack.pop() 
                multiple = current_slice* prev_num
                current_slice = prev_slice  +  multiple
                
            else:
                current_slice =  current_slice + s[idx]
                
        return current_slice
            