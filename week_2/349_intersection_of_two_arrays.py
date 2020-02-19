class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        for num1 in nums1:
            for num2 in nums2:
                if (num1 == num2 and num1 not in answer):
                    answer.append(num1)
        return answer
        
