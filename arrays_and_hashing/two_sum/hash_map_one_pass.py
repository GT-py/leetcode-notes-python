"""
Time: O(n)
Space: O(n)
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in prevMap:
                return [prevMap, i]
            prevMap[num] = i