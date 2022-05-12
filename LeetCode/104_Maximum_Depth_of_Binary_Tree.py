class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

# T: O(n), S: O(n)
# ******BFS*******

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:        
        # ****Breath for search*********************
        if not root:
            return 0
        level = 0
        q = [root]
        while q:
            tq = []
            for n in q:
                if n.left:
                    tq.append(n.left)
                if n.right:
                    tq.append(n.right)
            q = tq
            level += 1
        return level