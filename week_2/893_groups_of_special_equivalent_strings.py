from collections import defaultdict 

class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        group = []
        for word in A:
            i = 0
            even = []
            odd = []
            while i < len (word):
                if (i % 2 == 0):
                    even.append(word[i])
                else:
                    odd.append(word[i])
                i += 1
            combined = "".join(sorted(even) + sorted(odd))
            if combined not in group:
                group.append(combined)
        return len(group)
