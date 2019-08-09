class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        index = 0
        end = len(nums)
        while index < end:
            if nums[index] == 0:
                nums.append(nums.pop(index))
                end -= 1
            else:
                index += 1
