class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Time: O(nlogn + mlogm)
        Space: O(1) or O(n+m) depending on the sorting algorithm
        """
        n = len(s)
        if n != len(t):
            return False
        return sorted(s) == sorted(t)