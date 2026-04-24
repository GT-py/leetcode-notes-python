"""
Time: O(n)
Space: O(n)
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, num in enumerate(nums):
            indices[num] = i
        for i, num in enumerate(nums):
            diff = target - num
            if indices in diff and i != indices[diff]:
                return [i, indices[i]]
        return []