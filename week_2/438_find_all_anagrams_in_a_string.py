from collections import Counter

class Solution: 
    
    def isEqualCounters(self, actualCounter: Counter(), tempCounter: Counter()) -> bool:
        for key, value in actualCounter.items():
            if tempCounter[key] != actualCounter[key]:
                return False
        return True
    
    def isInCounter(self, counterCount : Counter(), key: str) -> bool:
        for k in counterCount:
            if k == key:
                return True
        return False
        
    def findAnagrams(self, s: str, p: str) -> List[int]:
        output = []
        p_counter = Counter(p)
        left_window = 0
        right_window = len(p) - 1
        temp = Counter(s[left_window: right_window + 1])
        right_window += 1
        while right_window <= len(s):
            if self.isEqualCounters(p_counter, temp):
                output.append(left_window)
            if right_window >= len(s):
                return output
            temp[s[left_window]] -= 1
            if self.isInCounter(temp, s[right_window]):
                temp[s[right_window]] += 1
            else:
                temp.update({s[right_window]:1})
            left_window += 1
            right_window += 1
        return output
        
        
