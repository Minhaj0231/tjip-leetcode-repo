# TC: O(N)  Here N = len  of the    stirngs  in the input array
# MC: O(N*M) Here N = len  of the stirngs  in the input array and M = size of the input array 

class Solution:
    def stringDiffer(self,  strings):
        for  i in range (len(strings[0])):
            visited_patterns = set()

            for j in range(len(strings)): 
                temp_char =   strings[j][:i] + strings[j][i+1:]
                if temp_char in visited_patterns:
                    return True
                else:
                    visited_patterns.add(temp_char)
        return False
            
