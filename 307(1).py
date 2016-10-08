class Node(object):
    def __init__(self,val,begin,end):
        self.val,self.begin,self.end=val,begin,end
        self.left,self.right=None,None
    

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums[:]
        self.root = Node(0,0,len(nums))
        self.buildtree(self.root,nums)
    
    def buildtree(self,root,nums):
        if root.begin != root.end:
            root.left = Node(0,root.begin,(root.begin+root.end)/2)
            self.buildtree(root.left,nums)
            root.right = Node(0,(root.begin+root.end)/2+1,root.end)
            self.buildtree(root.right,nums)
            root.val = root.left.val+root.right.val
        else:
            if root.begin < len(self.nums):
                root.val = nums[root.begin]
            else:
                root.val = 0
            
    def updatetree(self,root,i,dif):
        if root == None: return
        if root.begin <= i <= root.end:
            root.val += dif
            self.updatetree(root.left,i,dif)
            self.updatetree(root.right,i,dif)
        else: return
        
    def sumtree(self,root,i,j):
        if root == Node: return 0
        if i > root.end or j < root.begin:
            return 0
        elif i == root.begin and j == root.end:
            return root.val
        elif j<=(root.begin + root.end)/2:
            return self.sumtree(root.left,i,j)
        elif i > (root.begin + root.end)/2:
            return self.sumtree(root.right,i,j)
        else:
            return self.sumtree(root.left,i,(root.begin + root.end)/2) + self.sumtree(root.right,(root.begin + root.end)/2+1,j)

    def update(self, i, val):
        
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        dif,self.nums[i] = val-self.nums[i],val
        self.updatetree(self.root,i,dif)
                
        
    
    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sumtree(self.root,i,j)
