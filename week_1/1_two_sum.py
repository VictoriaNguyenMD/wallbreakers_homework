
from collections import defaultdict

class Solution:
    def twoSum(self, array, target):
      """
      :type array: List[int]
      :type target: int
      :rtype: Tuple(int)
      """
      dict_key_index = defaultdict(list)

      for index, key in enumerate(array):
        complement = target - key
        if complement in dict_key_index:
          return (dict_key_index.get(complement)[0], index)
        else:
          dict_key_index[key].append(index)

      return "No Two Sum"


