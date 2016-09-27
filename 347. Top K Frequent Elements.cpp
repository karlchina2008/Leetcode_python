"""
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].
"""
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict={}
        for num in nums:
            if num not in dict:dict[num]=1
            else: dict[num]+=1
        return map(lambda x:x[0],sorted(dict.items(),key=lambda y:-y[1])[:k])
