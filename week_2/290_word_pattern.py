from collections import defaultdict

#Tough Problem. A lot of edge cases

class Solution:
    def getWord(self, s: str, i: int) -> str:
        output = ""
        temp_i = i
        while (temp_i < len(s) and s[temp_i] != " "):
            output += s[temp_i]
            temp_i += 1
        while (temp_i < len(s) and s[temp_i] == " "):
            temp_i += 1
        return output, (temp_i - i)
    
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = set()
        dict_match = defaultdict(lambda: "")
        i = 0
        for char in pattern:
            word, increment = Solution().getWord(str, i)
            if (char in dict_match):
                if (dict_match[char] != word):
                    return False
            else:
                if word in words or word == "":
                    return False
                words.add(word)
                dict_match[char] = word
            i += increment
        if i != len(str):
            return False
        return True
        
