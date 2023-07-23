# All possible Full Binary Trees

# Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.

# Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.

# A full binary tree is a binary tree where each node has exactly 0 or 2 children.
# Example 1:

# Input: n = 7
# Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
# Example 2:

# Input: n = 3
# Output: [[0,0,0]]

# Constraints:

# 1 <= n <= 20

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def allPossibleFBT(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n%2 == 0 or n < 1:
            return []
        dp=[ [] for _ in range(n + 1)]
        dp[1]=[TreeNode(0)]
        for i in range(3,n+1):
            for j in range(1,i):
                leftTree=dp[j]
                rightTree=dp[i-1-j]
                for leftSubtree in leftTree:
                    for rightSubtree in rightTree:
                        root=TreeNode(0)
                        root.left=leftSubtree
                        root.right=rightSubtree
                        dp[i].append(root)
        return dp[n]                    
