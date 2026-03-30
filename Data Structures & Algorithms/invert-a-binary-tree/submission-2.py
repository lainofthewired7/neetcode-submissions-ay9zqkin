# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:

            return None

        stack = []

        def traverse(root):

            if not root:

                return

            stack.append(root)

            traverse(root.left)

            traverse(root.right)

        traverse(root)

        while stack:

            curr = stack.pop()

            curr.left, curr.right = curr.right, curr.left

        return root

    

        

        

        
        