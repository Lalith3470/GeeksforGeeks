class Solution:
    
    #Function to rotate matrix anticlockwise by 90 degrees.
    def rotateby90(self,a, n): 
        # code here
        lst=[]
        for i in zip(*a):
            lst.append(i)
        a[:]=lst[::-1]

