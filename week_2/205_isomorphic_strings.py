from collections import defaultdict

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        count_s = defaultdict(int)
        count_t = defaultdict(int)
        s_i, t_i = 0, 0
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                if s[i] not in count_s:
                    count_s[s[i]] = s_i
                    s_i += 1
                if t[i] not in count_t:
                    count_t[t[i]] = t_i
                    t_i += 1
        for i in range(len(t)):
            if (count_s[s[i]] != count_t[t[i]]):
                return False
        return True
