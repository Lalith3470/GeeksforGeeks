
class Solution:
    def findSubArraySum(self, Arr, N, k):
        # code here
        cnt=0
        sm=0
        dic={}
        for i in Arr:
            sm+=i
            if sm==k:cnt+=1
            if sm-k in dic:
                cnt+=dic[sm-k]
            if sm in dic:   
                dic[sm]+=1
            else:
                dic[sm]=1
        return cnt
            
