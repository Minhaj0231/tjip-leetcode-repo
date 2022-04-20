# TC: O(N*MlogM) Here N=lenght of the array   M=maximax size  of the strings in the array  
# MC: O(N) 
class Solution:
    def isAnagram(self, s, t):
        s_dict = {}
        for idx in range (0, len(s)):
            if  s[idx] in  s_dict:
                s_dict[s[idx]]+=1
            else:
                s_dict[s[idx]] = 1       
        for idx in range(0, len(t)):
            if t[idx] not in s_dict:
                return False
        
            else: 
                s_dict[t[idx]]  -=1
              
        for  value in s_dict.values():
            if value != 0:
                return False
            
        return True



# TC: O(N*MlogM)  N= total number of characters in all the input in  the input List 
# MC: O(N) 
class Solution:
    def groupAnagrams(self, strs):
        
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