class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp_list = set(nums)
        if len(temp_list) == len(nums):
            return False
        else:
            return True