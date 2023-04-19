
class Solution:
    def countDistinct(self, A, N, K):
        # Code here
        dic={}
        lst=[]
        cnt=0
        for i in range(N):
            cnt+=1
            if A[i] not in dic:
                dic[A[i]]=1
            else:
                dic[A[i]]+=1
            if cnt>=k:
                lst.append(len(dic))
                dic[A[i+1-k]]-=1
                if dic[A[i+1-k]]==0:
                    dic.pop(A[i+1-k])
        return lst
