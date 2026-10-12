class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, j in enumerate(nums):
            comp = target - j
            if comp in seen:
                return [seen[comp], i]
            seen[j] = i # key = numbs add to target, vals = pos
