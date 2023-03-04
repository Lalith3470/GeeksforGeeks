class Solution:
    def longestSubstrDistinctChars(self, S):
        # code here
        mx=0
        for i in range(len(S)):
            a=S[i]
            for j in range(i+1,len(S)):
                if S[j] not in a:
                    a+=S[j]
                else:break
            mx=max(mx,len(a))
        return mx
