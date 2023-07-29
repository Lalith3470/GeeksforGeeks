#User function Template for python3
import math
def findMedian(root):
    # code here
    # return the median
    lst=[]
    def dfs(root):
        if root.left:dfs(root.left)
        lst.append(root.data)
        if root.right:dfs(root.right)
    dfs(root)
    if len(lst)%2!=0:
        return lst[len(lst)//2]
    ans=(lst[len(lst)//2]+lst[len(lst)//2-1])/2
    return int(ans) if int(ans)==math.ceil(ans) else ans
