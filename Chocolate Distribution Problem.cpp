class Solution{
    public:
    long long findMinDiff(vector<long long> a, long long n, long long m){
        //code
        long long int mn=INT_MAX;
        sort(a.begin(),a.end());
        for(long long i=0; i<=n-m;i++){
            mn=min(mn,a[m-1+i]-a[i]);
        }
        return mn;
    
    }   
};
