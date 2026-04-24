class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Time: O(nlogn)
        Space: O(n)
        そのままソートしてしまうと添え字情報がなくなる．
        """
        A = []
        for i in range(len(nums)):
            A.append([nums[i], i])
        i = 0
        j = len(nums) - 1
        while i < j:
            cur = A[i][0] + A[j][0]
            if cur == target:
                return [min(A[i][1], A[j][1]), max(A[i][1], A[j][1])]
            elif cur < target:
                i += 1
            else:
                j -= 1
        return []