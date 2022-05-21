class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        
        inorder(root)
        return res

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output, stack = [], []
        while (stack or root):
            if root:
                # Go to the left most and push the parent into the stack
                # We need this parent node once we are done with left child and need to go to the right child. 
                stack.append(root)
                root = root.left
            elif stack and root == None:
                # We are done with left, so pop out the parent
                root = stack.pop()
                output.append(root.val)
                # Go to the right child
                root = root.right
        return output

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        result = []
        while root is not None or stack != []:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result