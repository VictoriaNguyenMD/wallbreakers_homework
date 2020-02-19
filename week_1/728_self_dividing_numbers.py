class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        output = []
        while left <= right:
            found = True
            digits = str(left)
            for i in digits:
                if i == "0" or left % int(i) != 0:
                    found = False
                    break
            if found == True:
                output.append(left)
            left += 1
        return output
                    
                
                    
                    
        
