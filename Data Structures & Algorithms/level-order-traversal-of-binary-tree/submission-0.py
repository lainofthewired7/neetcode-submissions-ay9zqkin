# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        q = deque()

        ret = []

        if root:

            q.append(root)

        while q:

            lst = []

            for _ in range (len(q)):

                curr = q.popleft()

                lst.append(curr.val)

                if curr.left:

                    q.append(curr.left)

                if curr.right:

                    q.append(curr.right)

            ret.append(lst)

        return ret


        
        