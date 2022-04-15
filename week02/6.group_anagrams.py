class Solution:
    def groupAnagrams(self, strs) :
        
        groups = {}
        
        for  string in strs:
            sorted_str_lst = sorted(string)
            sorted_str = "".join(sorted_str_lst)
            if sorted_str in  groups:
                group_list = groups[sorted_str]
                group_list.append(string)
                groups[sorted_str] = group_list
            else:
                groups[sorted_str] = [string]
                      
        return groups.values()
        