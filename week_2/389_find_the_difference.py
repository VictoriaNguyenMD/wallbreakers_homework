from collections import defaultdict

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter = defaultdict(int)
        for char in t:
            counter[char] += 1
        for char in s:
            if char in counter:
                counter[char] -= 1
        for key, value in counter.items():
            if value != 0:
                return (key)
        return ""
            
        
