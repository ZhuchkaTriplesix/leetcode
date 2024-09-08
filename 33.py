class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = 0
        for i in nums:
            if i != target:
                index += 1
            else:
                return index
        if index == len(nums):
            return -1