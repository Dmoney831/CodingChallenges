class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True

        def dfs(root):
            if root is None:
                return 0
            return max(dfs(root.left),dfs(root.right))+1

        return abs(dfs(root.left)-dfs(root.right))<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root: return [True, 0]
            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.Bal = True
        def dfs(root):
            if not root: return 0
            left, right = dfs(root.left), dfs(root.right)
            if abs(left - right) > 1: 
                self.Bal = False
            return max(left, right) + 1
        
        dfs(root)
        return self.Bal

# ************Time Complexity: O(n) **************
# &***********Space Complexity: O(h) where h is height.
