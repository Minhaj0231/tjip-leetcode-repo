# TC: O(N)  Here N = all character in the input string array 
# MC: O(N)   
class Solution:
    def group_strings(self, words):

        groups = {}

        for word in words:
            word_pattern = self.get_pattern(word)

            if word_pattern in groups:
                pattern_list = groups[word_pattern]
                pattern_list.append(word)
                groups[word_pattern] = pattern_list
            else:
                pattern_list =  [word]
                groups[word_pattern] = pattern_list
        return groups

    def get_pattern(self, word):
        pattern = ""
        for  i in range(1, len(word)):
            value =  ord(word[i]) - ord(word[0])
            if value < 0:
                value += 26
            pattern += chr(value + ord('a'))
        return pattern


            
            

        