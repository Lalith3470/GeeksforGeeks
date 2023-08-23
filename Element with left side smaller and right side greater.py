def findElement( arr, n):
    res=-1
    mx=arr[0]
    for i in range(1,n):
        if arr[i]<mx:
            res=-1
        elif arr[i]>=mx:
            if res==-1 and i!=n-1:
                res=arr[i]
            mx=arr[i]
    return res
