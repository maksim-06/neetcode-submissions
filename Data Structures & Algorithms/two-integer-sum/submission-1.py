class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dictionary = {nums[0] : 0}
        # answ = []
        # for i in range(1, len(nums)):
        #     for key, value in dictionary.items():
        #         if nums[i] + key == target:
        #             return [value, i]
                
        #     dictionary[nums[i]] = i

        dictionary = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in dictionary:
                return [dictionary[difference], i]
            dictionary[nums[i]] = i

