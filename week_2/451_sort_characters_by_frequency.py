from collections import defaultdict

class Solution:
    def frequencySort(self, s: str) -> str:
        counter = defaultdict(int)
        for char in s:
            counter[char] += 1
        sorted_dict = {key: value for key, value in sorted(counter.items(), key=lambda elem:elem[1], reverse = True)}
        output = ""
        for key, val in sorted_dict.items():
            output += (key * val)
        return output
            
    
