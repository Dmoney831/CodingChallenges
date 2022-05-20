class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False
        
        if self.sameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
        
    
    def sameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right))
        return False
    

class Solution:
def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    def traverse_tree(s):
        if s:
            return f"#{s.val} {traverse_tree(s.left)} {traverse_tree(s.right)}"
        return None
    string_s = traverse_tree(root)
    string_t = traverse_tree(subRoot)
    if string_t in string_s:
        return True
    return False
# Time Complexity: O(n + m) where n is root and m is subRoot.


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(p, q):
            if p and q:
                return (p.val == q.val and sameTree(p.left, q.left) and sameTree(p.right, q.right))
            return p is q
        
        if not subRoot: return True
        if not root: return False
        
        if sameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))        

# Time Complexity: O(|n| * |m|) where n is root and m is subRoot.