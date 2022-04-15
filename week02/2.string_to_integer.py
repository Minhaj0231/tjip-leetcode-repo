class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        sign = 1  
        boundary = int(math.pow(2,31))
        int_value = 0
        
        number_pos = -1
        idx = 0
        while idx < len(s):
            if s[idx] == "+":
                number_pos = idx+1
            elif s[idx] == '-':
                sign = -1 
                number_pos = idx+1
            elif s[idx].isdigit():
                number_pos =idx
                
            while number_pos != -1 and number_pos < len(s):
                if not s[number_pos].isdigit():
                    break 
                int_value = int_value*10 + int(s[number_pos])
                number_pos+=1
                if int_value > boundary:
                    int_value = boundary
                    break
                    
            if not s[idx].isspace() or number_pos>=0:
                break
                
            idx+=1
            
        int_value =  int_value*sign 
        int_value = min(int_value, boundary-1)           
        return int_value