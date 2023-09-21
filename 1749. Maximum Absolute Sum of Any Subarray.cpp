class Solution {
public:

    int maxAbsoluteSum(vector<int>& nums) {
        int mx=0,sm=0;
        for(auto i:nums){
            sm+=i;
            if(sm<0) sm=0;
            if(sm>mx) mx=sm;
        }
        int min=0,sm1=0;
        for(auto i:nums){
            sm1+=i;
            if(sm1<min) min=sm1;
            if(sm1>0) sm1=0;
        }
        return max(mx,abs(min));
    }
};
