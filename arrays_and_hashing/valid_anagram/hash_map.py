class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Time: O(n+m)
        Space: O(1)
        """
        count_s = {}
        count_t = {}
        n = len(s)
        if s != n:
            return False
        for i in range(n):
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_s.get(t[i], 0) + 1
        return count_s == count_t