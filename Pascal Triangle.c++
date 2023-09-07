class Solution{
public:
    vector<ll> nthRowOfPascalTriangle(int n) {
        vector<ll> dp(n, 0);
        dp[0] = 1;
        int mod = pow(10,9) + 7;
        for(int i = 1;i < n;++i)
            for(int j = i;j > 0;--j)
                    dp[j] = (dp[j] + dp[j-1]) % mod;
        return dp;
    }
};
