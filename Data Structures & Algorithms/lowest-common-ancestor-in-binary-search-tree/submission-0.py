# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if not root:

            return None

        curr = root

        LCA = root

        while curr:

            if p.val > curr.val and q.val > curr.val:

                curr = curr.right

                LCA = curr

            elif p.val < curr.val and q.val < curr.val:

                curr = curr.left

                LCA = curr

            elif curr.val == p.val:

                LCA = curr

                break

            elif curr.val == q.val:

                LCA = curr

                break
            
            else:

                break

        return LCA

                

            


    


        