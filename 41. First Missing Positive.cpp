"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        myset=set([])
        for num in nums:
            if num>0:
                myset.add(num)
        if 1 not in myset:return 1
        res=0xffffffff
        for num in myset:
            if num-1>0 and (num-1 not in myset):
                res=min(res,num-1)
            if (num+1) not in myset:
                res=min(res,num+1)
        return res
