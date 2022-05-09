# TC: O(N)  Here N = len  of the input string
# MC: O(N) 
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        numbers = [1]
        
        number_2_pos = 0
        number_3_pos = 0
        number_5_pos = 0
        
        for idx in range(n-1):
            
            number_2_multiple = numbers[number_2_pos]*2
            number_3_multiple = numbers[number_3_pos]*3
            number_5_multiple = numbers[number_5_pos]*5
            
            minimum_number = min(number_2_multiple, min(number_3_multiple,number_5_multiple))
            numbers.append(minimum_number)
            
            if minimum_number ==  number_2_multiple:
                number_2_pos +=1
            
            if minimum_number ==  number_3_multiple:
                number_3_pos +=1
            
            if minimum_number ==  number_5_multiple:
                number_5_pos +=1
                
        return numbers[len(numbers)-1]