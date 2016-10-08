class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.n=len(nums)
        self._nums=[0 for i in range(self.n)]
        #nums_cy=nums[:]
        self.record=[0 for i in range(self.n+1)]
        for i in range(self.n):
            self.update(i,nums[i])
    
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        dif,self._nums[i],i=val-self._nums[i],val,i+1
        while i<=self.n:
            self.record[i]+=dif
            i+=i&(-i)
        
    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        sum_i,sum_j,j=0,0,j+1
        while i>0:
            sum_i+=self.record[i]
            i-=i&(-i)
        while j>0:
            sum_j+=self.record[j]
            j-=j&(-j)
        return sum_j-sum_i
