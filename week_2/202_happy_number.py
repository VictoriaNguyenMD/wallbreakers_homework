class Solution:
    def isHappy(self, n: int) -> bool:
        str_num = str(n)
        int_sum = 0
        tracking = set()
            
        while (True):
            for digit in str_num:
                int_sum += (int(digit) * int(digit))
            if int_sum in tracking:
                return False
            elif int_sum == 1:
                return True
            else:
                tracking.add(int_sum)
                str_num = str(int_sum)
                int_sum = 0
