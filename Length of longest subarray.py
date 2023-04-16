#User function Template for python3

def longestSubarry( A, N):
    mx=0
    ln=0
    for i in range(N):
        if A[i]<0:
            mx=max(ln,mx)
            ln=0
        else:
            ln+=1
    return max(mx,ln)
    
