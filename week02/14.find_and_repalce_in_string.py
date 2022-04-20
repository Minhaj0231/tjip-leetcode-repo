# TC: O(N + L*smax) here N = len of the input string, L=  len of hte sources array, and smax - maximum lengthn of string in source array   
# MC: O(N) 
class Solution:
    def findReplaceString(self, s, indices, sources, targets):
        
        indices_dict = {}
        for idx in range(0, len(indices)):
            if  s[indices[idx]:].startswith(sources[idx]) :
                
                indices_dict[indices[idx]] = idx
                       
        letter_arr =  []
        idx = 0
        next_indices = 0
        
        while idx < len (s) and next_indices< len(sources):
            if idx in indices_dict:
                 
                letter_arr.append(targets[indices_dict[idx]])
                idx += len (sources[indices_dict[idx]])
                next_indices +=1
                
            else:
                letter_arr.append(s[idx])
                idx+=1
                
        while idx < len(s):
            letter_arr.append(s[idx])
            idx+=1
                   
        return "".join(letter_arr)