"""
Find the sum of all left leaves in a given binary tree.
"""
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        elif root.left and root.left.right==None and root.left.left==None:
            return root.left.val+self.sumOfLeftLeaves(root.right)
        else:
            return self.sumOfLeftLeaves(root.right)+self.sumOfLeftLeaves(root.left)
