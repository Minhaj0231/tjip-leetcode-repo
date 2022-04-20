# TC: O(n*MLogM) here n is the  len of the input array and M == maximum size of the strings.
# MC: O(n) 
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        def cmpS(a,b):  
            
            x = a+b
            y = b+a
            if x> y:
                return -1
            else:
                return 1
          
        if sum(nums) == 0:
            return str(0)
            
        for i in range(0, len(nums)):
            nums[i] = str(nums[i])

        nums = sorted(nums, key = functools.cmp_to_key(cmpS))            
        ans = "".join(nums) 
        
        return ans

      