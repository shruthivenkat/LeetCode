# 169. Majority Element

class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    dict_list = {}
    for i in nums:
      if i in dict_list:
        dict_list[i] += 1
      else:
        dict_list[i] = 1
    if dict_list[max(dict_list, key=dict_list.get)] >= math.floor(len(nums)/2):
      return max(dict_list, key=dict_list.get)