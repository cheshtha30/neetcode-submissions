# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#inorder is  -> left , root , right 
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(Node):
         
            while Node is None :
                return 

            inorder(Node.left)
            ans.append(Node.val)
            inorder(Node.right)
        ans = []
        inorder(root)
        return ans 