class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        set_candies = set(candies)
        len_set = len(set_candies)
        
        if (len_set <= len(candies)//2):
            return len_set
        else:
            return len(candies)//2
 
