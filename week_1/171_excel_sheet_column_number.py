class Solution:
    def titleToNumber(self, s: str) -> int:
        chars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        output = 0
        for i, char in enumerate(s[::-1]):
            output = output + (chars.index(char) + 1) * (26 ** i)
        return outputy
