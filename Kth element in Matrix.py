#User function Template for python3

def kthSmallest(mat, n, k): 
    # Your code goes here
    lst=[]
    for i in mat:
        lst+=i
    lst.sort()
    return lst[k-1]
