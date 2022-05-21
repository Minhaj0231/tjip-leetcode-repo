# TC: O(N)  Here N = len  of the input string
# MC: O(1) 
class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            "I":[1,1],
            "V":[2,5],
            "X": [3,10],
            "L": [4,50],
            "C": [5,100],
            "D": [6,500],
            "M": [7,1000]
        }
        
        total = 0
        i = 0
        while i < len(s):
            if i+1 < len(s) and symbols[s[i]][0] < symbols[s[i+1]][0]:
    
                value = symbols[ s[i+1]][1] - symbols[s[i]][1]
                total += value
                i +=2
            else: 
                total += symbols[s[i]][1]
                i+= 1
        return total
                