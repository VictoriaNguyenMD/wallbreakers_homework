from collections import defaultdict

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        complete = set (range(1, len(nums) + 1))
        counter = defaultdict(int)        
        output = []
        for num in nums:
            counter[num] += 1
        for key, value in counter.items():
            if value == 2:
                output.append(key)
        difference = list(complete - set(nums))
        output += difference
        return (output)
        
