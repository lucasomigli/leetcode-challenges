class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        l = []
        for num in nums:
            if num in l:
                l.remove(num)
            else:
                l.append(num)
        return l.pop()
