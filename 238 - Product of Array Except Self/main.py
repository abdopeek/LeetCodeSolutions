import math
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = []
        product = math.prod(nums) 
        for i in range(len(nums)):
            if nums[i] == 0:
                ans.append(math.prod(nums[:i] + nums[i+1:]))
            else:
                ans.append(product//nums[i])
        return ans
