# TC: O(N) here n is the  len of the input string
# MC: O(1) 
class Solution:
    def minWindow(self, s,t):
        
        freq = [0]*130
        
        for  char in t:
            freq[ord(char)] +=1  
            
        min_len = float('inf');
        left = 0
        right = 0
        start_index = -1
        remaining_char = len(t)
        
        while right < len(s):
            if  freq[ord(s[right])]>0:
                remaining_char -=1
            freq[ord(s[right])] -=1
            right +=1
            
            while remaining_char == 0:    
                if min_len > (right -left):
                    min_len = right - left
                    start_index = left
                    
                if freq[ord(s[left])]==0:
                    remaining_char +=1
                    
                freq[ord(s[left])] +=1
                left +=1    
                
        if start_index == -1:
            return ""
        return s[start_index: start_index+min_len]
    