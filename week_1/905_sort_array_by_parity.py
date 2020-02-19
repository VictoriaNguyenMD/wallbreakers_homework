class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        int_first = 0
        int_last = len(A) - 1
        
        while int_first < int_last and int_first < len(A) and int_last >= 0:
            if (A[int_first] % 2 == 0):
                int_first += 1
            else:
                int_temp = A[int_first]
                A[int_first] = A[int_last]
                A[int_last] = int_temp
                int_last -= 1
        return A
        
        
