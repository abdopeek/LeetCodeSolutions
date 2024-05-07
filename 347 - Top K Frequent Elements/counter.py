from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        kfreq = counter.most_common(k)
        ans = [x[0] for x in kfreq]
        return ans
