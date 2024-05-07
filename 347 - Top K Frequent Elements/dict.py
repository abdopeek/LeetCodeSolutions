class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dict = {}
        res = []
        for num in nums:
            if num in dict.keys():
                dict[num] += 1
            else:
                dict[num] = 1
        for i in range(k):
            res.append(max(dict, key=lambda s: dict[s]))
            del dict[res[-1]]
        return res
