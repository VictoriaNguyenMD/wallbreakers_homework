class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        caps = 0
        for letter in word:
            if (letter >= 'A' and letter <= 'Z'):
                caps += 1
        if word[0] >= 'A' and word[0] <= 'Z' and caps == 1:
            return True
        elif caps == len(word) or caps == 0:
            return True
        return False

