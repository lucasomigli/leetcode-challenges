class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, val in enumerate(nums):
            c = target - val
            if nums[index+1:].count(c) > 0:
                c_index = nums[index+1:].index(target - val)
                return [index, c_index+index+1]
