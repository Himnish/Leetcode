# Minimum ASCII Delete Sum for Two Strings
# Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.
  
# Example 1:
# Input: s1 = "sea", s2 = "eat"
# Output: 231
# Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
# Deleting "t" from "eat" adds 116 to the sum.
# At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.

# Example 2:
# Input: s1 = "delete", s2 = "leet"
# Output: 403
# Explanation: Deleting "dee" from "delete" to turn the string into "let",
# adds 100[d] + 101[e] + 101[e] to the sum.
# Deleting "e" from "leet" adds 101[e] to the sum.
# At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
# If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.

# Constraints:
# 1 <= s1.length, s2.length <= 1000
# s1 and s2 consist of lowercase English letters.

class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        def total_ascii(s):
            return sum([ord(c) for c in s])

        def lcs_ascii(s1, s2):
            nrows = len(s1) + 1
            ncols = len(s2) + 1
            memo = [[0] * ncols for _ in range(nrows)]
            for r in range(1, nrows):
                for c in range(1, ncols):
                    if s1[r-1] == s2[c-1]:
                        memo[r][c] = memo[r-1][c-1] + ord(s1[r-1])
                    else:
                        memo[r][c] = max(memo[r-1][c], memo[r][c-1])
            return memo[nrows-1][ncols-1]
        
        lcs = lcs_ascii(s1, s2)
        return total_ascii(s1) + total_ascii(s2) - lcs*2
