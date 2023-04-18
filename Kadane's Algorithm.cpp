class solution{
  public:
    // arr: input array
    // n: size of array
    //Function to find the sum of contiguous subarray with maximum sum.
    long long maxSubarraySum(int arr[], int n){
        
        // Your code here
        long long sm=0,mx=arr[0];
        for(int i=0;i<n;i++){
            sm+=arr[i];
            if(sm>mx){mx=max(sm,mx);}
            if(sm<0)sm=0;
        }
        return mx;
    }
};
