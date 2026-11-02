class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        len_nums = len(nums)
        set_nums = set(nums)
        if len(set_nums) == len_nums:
            return False
        return True


        # spisok = []
        # f=0
        # for i in nums:
        #     if i not in spisok:
        #         spisok.append(i)
        #     else:
        #         f=1
        #         return True
        # if f == 0:
        #     return False
