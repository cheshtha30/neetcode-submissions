# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(Node):
            if Node is None:
                return 0
            depth_left = dfs(Node.left)
            depth_right = dfs(Node.right)

            depth = 1 + max(depth_left , depth_right)
            return depth 



        return dfs(root)
        

        