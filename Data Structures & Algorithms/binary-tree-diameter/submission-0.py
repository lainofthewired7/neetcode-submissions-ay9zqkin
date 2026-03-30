# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.maxD = 0

        def traverse(node):

            if not node:

                return 0

            leftHeight = traverse(node.left)

            rightHeight = traverse(node.right)

            d = leftHeight + rightHeight

            self.maxD = max(d, self.maxD)

            return max(leftHeight, rightHeight) + 1

        traverse(root)

        return self.maxD
        