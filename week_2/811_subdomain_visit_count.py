from collections import defaultdict

class Solution:
    def print_count(self, counter: defaultdict(int)) -> List[str]:
        output = []
        for key, val in counter.items():
            string = ""
            string += str(val) + " " + key
            output.append(string)
        return (output)
    
    def ft_strchr(self, string: str, c: str) -> int:
        for index, char in enumerate(string):
            if (char == c):
                return index
        return len(string) + 1
    
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter = defaultdict(int)
        
        for word in cpdomains:
            i = 0
            increment = self.ft_strchr(word, " ")
            times = int(word[:increment])
            i += increment
            while (i < len(word)):
                i += 1
                increment = self.ft_strchr(word[i:], ".")
                counter[word[i:]] += times
                i += increment
        return self.print_count(counter)
            
            
            
            
            
            
        
