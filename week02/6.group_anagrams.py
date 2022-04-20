# TC: O(N*MlogM) N == size of the  array, M == maximum size of the strings.
# MC: O(N) 
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
        

# TC: O(M) here M is the total   nubmer of chareacter in the  input  array 
# MC: O(N) 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}
        
        for  string in strs:
            hash_value = self.getHash(string)
            if hash_value in  groups:
                group_list = groups[hash_value]
                group_list.append(string)
                groups[hash_value] = group_list
            else:
                groups[hash_value] = [string]
                      
        return groups.values()
    
    
    def getHash(self, string):
        hash_value = 1
        for char in  string:
            hash_value = hash_value * (257 + (ord(char) - ord("a")))         
        return hash_value