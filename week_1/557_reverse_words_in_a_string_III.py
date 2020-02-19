class Solution:
    def reverseWords(self, s: str) -> str:
        traverse = 0
        begin_char = 0
        output = []
        
        while traverse < len(s):
            while traverse < len (s) and s[traverse] != " ":
                traverse += 1
            end_char = traverse - 1
            while (end_char >= begin_char):
                output.append(s[end_char])
                end_char -= 1
            if (traverse < len(s)):
                output.append(" ")
            begin_char = traverse + 1
            traverse += 1
        return "".join(output)
        
