class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        mylist,i=[],0
        while i<len(s):
            if s[i]=='[':
                mylist.append(NestedInteger())
                i+=1
            elif s[i]==',': i+=1
            elif s[i]>='0' and s[i]<='9':
                temp=""
                while i<len(s) and s[i]>='0' and s[i]<='9':
                    temp,i=temp+s[i],i+1
                #print temp,mylist
                if len(mylist)==0:
                    return int(temp)
                else:
                    mylist[-1].add(NestedInteger(int(temp)))
            elif s[i]=='-':
                temp,i="",i+1
                while i<len(s) and s[i]>='0' and s[i]<='9':
                    temp,i=temp+s[i],i+1
                if len(mylist)==0:
                    return -int(temp)
                else:
                    mylist[-1].add(NestedInteger(-int(temp)))
            else:
                i+=1
                ni=mylist.pop()
                if len(mylist)==0:
                    return ni
                else:
                    mylist[-1].add(ni)
