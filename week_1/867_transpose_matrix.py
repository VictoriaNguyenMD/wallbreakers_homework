class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        new_A = [[0 for x in range(len(A))] for y in range(len(A[0]))]
        print(new_A)
        int_row = 0
        while (int_row < len(A)):
            int_col = 0
            while (int_col < len(A[0])):
                new_A[int_col][int_row] = A[int_row][int_col]
                int_col += 1
            int_row += 1
        return new_A

