# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def dfs(Node):
            if Node is None:
                return 0

            left_depth = dfs(Node.left)
            right_depth = dfs(Node.right)
            self.diameter = max(self.diameter, left_depth + right_depth)
            depth = 1 + max(left_depth , right_depth)
            return depth

        dfs(root)
        return self.diameter