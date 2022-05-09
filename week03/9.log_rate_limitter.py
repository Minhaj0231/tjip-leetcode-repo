# TC: O(N)  Here N = len  of the input string
# MC: O(M) Here M is the number of unique messages   
class Logger:

    def __init__(self):
        self.time= {
        }

    def shouldPrintMessage(self, timestamp, message):
        if  message in self.time: 
            if timestamp  -9 <= self.time[message]:
                return False
            
        self.time[message] = timestamp
        return True
                    



