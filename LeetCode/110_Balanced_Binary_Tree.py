class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True

        def dfs(root):
            if root is None:
                return 0
            return max(dfs(root.left),dfs(root.right))+1

        return abs(dfs(root.left)-dfs(root.right))<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)