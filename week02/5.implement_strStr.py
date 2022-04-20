# TC: O(N) here n is the  len of the input string
# MC: O(N) 
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        self.preProcessHash = [0]*(len(haystack)+1)
        self.po = [1]* len(self.preProcessHash)
        self.base = 29
        self. mod = 1000000007
        
        self. preProcess(haystack)
        needelHash = self.generateHash(needle)
        
       
        for i in range(0, len(haystack)- len(needle)+1):
            if self.getRangeHash(i, i+len(needle) -1) == needelHash:
                return i
        return -1
                 
    def preProcess(self, haystack):
        self.preProcessHash[0] =  ord(haystack[0])
                                
        for i in range (1, len(haystack)):
            self.preProcessHash[i] = (self.preProcessHash[i-1] * self.base) % self.mod
            self.preProcessHash[i] += ord(haystack[i])
            self.po[i] = (self.po[i-1]*self.base) % self.mod
    
    def generateHash(self, needle):
        needleHash = 0
        for idx in range(0, len(needle)):
            needleHash =  ((needleHash*self.base)% self.mod )+ ord(needle[idx]) 
        return needleHash
            
    def getRangeHash(self,l,r):
        right =  self.preProcessHash[r]
        left = 0
        
        if l!= 0:
            left =  self.preProcessHash[l-1]*self.po[r-l+1] % self.mod
        
        rangeHash = (right - left + self.mod) %self.mod
        
        return rangeHash
        