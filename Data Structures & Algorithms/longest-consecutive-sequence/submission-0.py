class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        nums = set(nums)
        c = 1
        g = 1
        for num in nums:
            if num - 1 not in nums:
                while num + g in nums:
                    c += 1
                    g += 1

                max_len = max(max_len, c)
                c = 1
                g = 1
        return max_len