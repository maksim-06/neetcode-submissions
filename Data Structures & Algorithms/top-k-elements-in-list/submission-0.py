class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        for i in range(len(nums)):
            if nums[i] not in dictionary:
                dictionary[nums[i]] = 0
            dictionary[nums[i]] += 1
        
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]

        for num, col in dictionary.items():
            buckets[col].append(num)
        
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for j in buckets[i]:
                res.append(j)
                if len(res) == k:
                    break
            if len(res) == k:
                break
        return res