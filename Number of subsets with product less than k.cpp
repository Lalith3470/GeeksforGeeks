
class Solution {
  public:
    void subs(int idx,int arr[],int n,int k,int &cnt,int pro){
        if(pro>k) return;
        if(idx==n){
            if(pro<=k) cnt++;
            return;
        }
        subs(idx+1,arr,n,k,cnt,pro);
        int val=arr[idx];
        subs(idx+1,arr,n,k,cnt,pro*val);
    }
    int numOfSubsets(int arr[], int N, int K) {
        // code here
        int cnt=0;
        int pro=1;
        subs(0,arr,N,K,cnt,pro);
        return cnt-1;
    }
};
