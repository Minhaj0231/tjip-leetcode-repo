# TC: O(N)  Here N = len  of the input string
# MC: O(N) 
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        isomorphic = self.match_char(s, t) and self.match_char(t,s)
        return isomorphic    
             
    def match_char(self, s, t):
        map = {}
        isomorphic = True 
        for i in range ( 0, len(s)):
            if   s[i] in map:
                 if map[s[i]] != t[i]:
                        isomorphic = False
                        break
            
            else:
                map[s[i]]  = t[i]
        
        return isomorphic