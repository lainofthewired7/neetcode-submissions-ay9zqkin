# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        self.goodNodesCount = 0

        def dfs (node, lastMax):

            if not node:

                return

            if node.val >= lastMax:

                self.goodNodesCount += 1

            dfs(node.left, max(lastMax, node.val))

            dfs(node.right, max(lastMax, node.val))

        dfs(root, float('-inf'))

        return self.goodNodesCount

            

            
        