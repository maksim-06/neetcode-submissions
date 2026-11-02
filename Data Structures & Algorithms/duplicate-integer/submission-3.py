class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        len_nums = len(nums)
        set_nums = set(nums)
        if len(set_nums) == len_nums:
            return False
        return True
