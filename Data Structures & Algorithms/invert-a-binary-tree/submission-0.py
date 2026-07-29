# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invertBinary(Node):
            while Node is None:
                return 

            Node.left, Node.right = Node.right, Node.left

            invertBinary(Node.left)
            invertBinary(Node.right)

        invertBinary(root)
        return root 

