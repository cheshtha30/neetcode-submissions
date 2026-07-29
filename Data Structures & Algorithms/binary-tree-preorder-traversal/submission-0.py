# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#preorder: root -> left -> right 
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def preorder(Node):
            while Node is None:
                return 

            ans.append(Node.val)
            preorder(Node.left)
            preorder(Node.right)
        preorder(root)
        return ans
