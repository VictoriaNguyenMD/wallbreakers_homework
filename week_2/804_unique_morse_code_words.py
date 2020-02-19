class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        moorse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        set_types = set()
        for word in words: 
            str_transform = ""
            for c in word:
                str_transform += moorse[ord(c) - ord('a')]                              
            set_types.add(str_transform)
        return len(set_types)
        
        
        
        
