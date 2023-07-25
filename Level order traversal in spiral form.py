from collections import deque
def findSpiral(root):
    # Code here
    lst=[]
    q=deque()
    q.append(root)
    c=0
    while q:
        levels=[]
        for i in range(len(q)):
            tmp=q.popleft()
            if tmp:
                levels.append(tmp.data)
                q.append(tmp.left)
                q.append(tmp.right)
        if levels:
            if c%2==0:
                lst+=levels[::-1]
            else:
                lst+=levels
        c+=1
    return lst
