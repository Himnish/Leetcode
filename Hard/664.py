# Strange Printer
# There is a strange printer with the following two special properties:

# The printer can only print a sequence of the same character each time.
# At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.
# Given a string s, return the minimum number of turns the printer needed to print it.

# Example 1:

# Input: s = "aaabbb"
# Output: 2
# Explanation: Print "aaa" first and then print "bbb".
# Example 2:

# Input: s = "aba"
# Output: 2
# Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.

# Constraints:
# 1 <= s.length <= 100
# s consists of lowercase English letters.

class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
				# Get the length of the input string
        length = len(s)
        # Matrix to store the minimum number of turns needed to print s[i:j+1]
        dp = [[0] * length for _ in range(length)]
        # Loop backwards over the matrix to fill upper diagonal
        for i in range(length-1, -1, -1):
            # Initialize the diagonal values to 1, since it takes one turn to print a single character
            dp[i][i] = 1
            # Loop forwards over the matrix to fill lower diagonal
            for j in range(i+1, length):
                # If s[i] and s[j] are the same character, we can print them in one turn
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j-1]
                else:
                    # If s[i] and s[j] are different characters, we try to use the previously computed dp values
                    # Update the current dp value by taking the minimum value of the two possible options
                    dp[i][j] = float('inf')
                    for k in range(i, j):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j])
        
        # The minimum number of turns needed to print the entire string s is stored in dp[0][length-1]
        return dp[0][length-1]
