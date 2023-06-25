class Solution{
public:
    bool isvalid(long long val){
        if(val<=1)return false;
        for(int i=2; i<=sqrt(val);i++){
            if(val%i==0)return false;
        }
        return true;
    }
public:
    long long primeProduct(long long L, long long R){
        // code here
        long long ans=1;
        for(long long i=L; i<=R; i++){
            if(isvalid(i))ans=ans*i%(1000000007);
        }
        return ans;
    }
};
