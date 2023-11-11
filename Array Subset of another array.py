#User function Template for python3
from collections import Counter
def isSubset( a1, a2, n, m):
    cnt=Counter(a1)
    cnt2=Counter(a2)
    for i,j in cnt2.items():
        if i not in cnt:
            return "No"
        elif j>cnt[i]:
            return "No"
    return "Yes"
    
