"""
Suppose you have a random list of people standing in a queue. 
Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.
"""
class Solution(object):
    
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        res=[]
        size=len(people)
        people=sorted(people,key=lambda x:x[1])
        people=sorted(people,key=lambda x:-x[0])
        #print people
        for p in range(0,size):
            if people[p][1]<p:
                res.insert(people[p][1],people[p])
            else:
                res.append(people[p])
        return res
