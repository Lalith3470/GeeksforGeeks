#User function Template for python3

def rotate(matrix): 
    #code here
    l=[]
    for i in zip(*matrix):
        l.append(i)
    matrix[:]=l[::-1]
