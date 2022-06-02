class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.res = max(self.res, left + right)
            
            return 1 + max(left, right)
        
        dfs(root)
        return self.ans

# *****Time Complexity: O(n)
# *****Space Complexity: O(h) where h is height.


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.ans = max(self.ans, left + right)
            return max(left, right) + 1
        
        if not root:
            return 0
        dfs(root)
        return self.ans