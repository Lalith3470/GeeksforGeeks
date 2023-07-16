class Solution:
    #Function to reverse the queue.
    def rev(self, q):
        #add code here
        l=[]
        for i in range(q.qsize()):
            l.append(q.get())
        while l:
            q.put(l.pop())
        return q
