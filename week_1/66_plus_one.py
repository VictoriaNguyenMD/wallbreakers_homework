class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        j = len(digits) - 1
        carry = 0
        digits[j] += 1
        while (j >= 0):
            num = digits[j] + carry
            if num >= 10:
                carry = num % 9
                digits[j] = 0
            else:
                digits[j] += carry
                carry = 0
            j -= 1
        
        if carry != 0:
            digits.insert(0, carry)
        return digits
            
