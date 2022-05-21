# TC: O(N^2)  Here N = len  of the input array
# MC: O(N^2) 
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        two_sum= {}
        size = len(nums1)  
        
        for i in range(size):
            for j in range(size):
                total = nums1[i] + nums2[j]
                
                if total  in  two_sum:
                    two_sum[total] += 1      
                else:
                    two_sum[total] = 1
                    
        foursum = 0
        for i in range(size):
            for j in range(size):
                total = nums3[i] + nums4[j]
                total *= -1
                
                if total in two_sum:
                    foursum += two_sum[total]
                    
        return foursum
                    