class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Time: O(n^2)
        Space: O(1)
        """
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
