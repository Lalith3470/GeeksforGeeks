
class Solution {
  public:
    //Function to return a list of indexes denoting the required 
    //combinations whose sum is equal to given number.
    void combs(int idx,vector<int>A,int target,int n,vector<int>&tmp,vector<vector<int>>&lst){
        if(idx==n){
            if(target==0){
                lst.push_back(tmp);
            }
            return;
        }
        if(A[idx]<=target){
            tmp.push_back(A[idx]);
            combs(idx,A,target-A[idx],n,tmp,lst);
            tmp.pop_back();
        }
        combs(idx+1,A,target,n,tmp,lst);
    }
    vector<vector<int> > combinationSum(vector<int> &A, int B) {
        // Your code here
        vector<vector<int>>lst;
        vector<int>tmp;
        sort(A.begin(),A.end());
        A.erase(unique(A.begin(),A.end()),A.end());
        combs(0,A,B,A.size(),tmp,lst);
        sort(lst.begin(),lst.end());
        if(!lst.empty()){
            return lst;
        }
    }
};
