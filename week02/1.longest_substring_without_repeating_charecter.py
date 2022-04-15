class Solution:
    def lengthOfLongestSubstring(self, s):
        
        if len(s) == 0 :
            return 0
        
        seen = set()
        start = 0
        end = 0
        max_size = 0
        current_size = 0
        
        seen.add(s[0])
        current_size+=1
        max_size +=1
        
        for idx in range (1, len(s)):
            while s[idx] in seen:
                seen.remove(s[start])
                start+=1
                current_size -=1 
            seen.add(s[idx])
            current_size +=1
            max_size = max(current_size, max_size)
        return max_size
                