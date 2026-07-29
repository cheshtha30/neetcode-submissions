# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#inorder = left -> root -> right
#preoerder = root -> left -> right
#postorder = left-> right -> root 
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def postorder(Node):
            while Node is None:
                return

            postorder(Node.left)
            postorder(Node.right)
            ans.append(Node.val)

        postorder(root)
        return ans 