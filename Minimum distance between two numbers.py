class Solution:
    def minDist(self, arr, n, x, y):
        a=-1
        b=-1
        diff=9999999
        for i in range(n):
            if arr[i] == x:
                a=i
            elif arr[i] == y:
                b=i
            if a != -1 and b != -1:
                 diff = min(diff,abs(b-a))
        if diff == 9999999:
            return -1
        return diff
