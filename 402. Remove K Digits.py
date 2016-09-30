class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        i=0
        num=list(num)
        #print "here"
        while k>0 and i<len(num)-1:
            if num[i]>num[i+1]:
                num.pop(i)
                k=k-1
                i=i-1 if i>=1 else 0
            else:i=i+1
        i=0
        while i<len(num) and num[i]=='0':i+=1
        #print num
        num=num[i:]
        
        if k>=len(num):
            return '0'
        else: 
            num=num[:(len(num)-k)]
        
        return ''.join(num)
