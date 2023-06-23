class Solution:
    def maxLen(self, n, arr):
        #Code here
        mxlen=0
        i=-1
        s=0
        d={}
        d[s]=i
        while i<n-1:
            i+=1
            s+=arr[i]
            if s not in d:
                d[s]=i
            else:
                size=i-d[s]
                if size>mxlen:
                    mxlen=size
        return mxlen
