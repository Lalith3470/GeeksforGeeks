from collections import Counter
class Solution:
    def firstNonRepeating(self, arr, n): 
        # Complete the function
        cnt=Counter(arr)
        for i in arr:
            if cnt[i]==1:return i
        return 0
