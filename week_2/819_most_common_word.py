from collections import defaultdict

class Solution:
    
    def isPunct (self, c: str) -> bool:
        return (c == "!" or c == "?" or c == "'" or c == "," or c == ";" or c == ".")
    
    def toLower(self, string: str) -> str:
        output = ""
        for char in string:
            if (char >= 'A' and char <= 'Z'):
                output += chr(ord(char) + (ord('a') - ord('A')))
            elif (self.isPunct(char)):
                output += " "
            elif (not self.isPunct(char)):
                output += char
        return output
            
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = self.toLower(paragraph).split()
        counter = defaultdict(int)
        banned = set(banned)
        for word in words:
            if word not in banned:
                counter[word] += 1
        max_v = 0
        out = ""
        for word, count in counter.items():
            if count > max_v:
                max_v = count
                out = word
        return out
                        
            
        
