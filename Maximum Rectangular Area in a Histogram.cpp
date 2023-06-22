class Solution
{
    public:
    //Function to find largest rectangular area possible in a given histogram.
    long long getMaxArea(long long arr[], int n){
        // Your code here
        long long mx=0;
        stack<long long>stack;
        for(int i=0; i<=n; i++){
            while(!stack.empty() && (i==n || arr[stack.top()]>=arr[i])){
                long long int hi=arr[stack.top()];
                stack.pop();
                long long int wt=0;
                if(stack.empty()) wt=i;
                else wt=i-stack.top()-1;
                mx=max(mx,hi*wt);
            }
            stack.push(i);
        }
        return mx;
    }
};
