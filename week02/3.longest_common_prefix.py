class Solution:
    def longestCommonPrefix(self, strs):
        
        if len(strs) == 1:
            return strs[0]
        
        startpos = -1
        endpos = -1
        min_len = float('inf')
        for idx in range(0, len(strs)):
            min_len = min(min_len, len(strs[idx]))
      
        for str_pos in range(0, min_len):
            
            all_true = True
            char_value = strs[0][str_pos]
            for idx in range(1, len(strs)):
                if (strs[idx][str_pos]) != char_value:
                    all_true = False
                    break
            if all_true:
                if startpos == -1:
                    startpos = str_pos
                endpos = str_pos
            else:
                break
                
        if startpos == -1:
            return ""
        else:
            return strs[0][startpos:endpos+1 ]
            