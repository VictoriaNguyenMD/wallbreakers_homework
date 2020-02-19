class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        int_count = 0
        for j in J:
            for s in S:
                if (j == s):
                    int_count += 1
        return int_count
