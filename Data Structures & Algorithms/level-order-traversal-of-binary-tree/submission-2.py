# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        ret = []

        depth = 0

        def dfs(node, depth):

            if not node:

                return

            if len(ret) == depth:

                ret.append([node.val])

            else:

                ret[depth].append(node.val)

            dfs(node.left, depth+1)

            dfs(node.right, depth+1)

        dfs(root, depth)

        return ret



            


        