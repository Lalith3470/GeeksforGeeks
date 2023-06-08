class Solution
{
public:
    string kthPermutation(int n, int k)
    {
        // code here
        string s = "";
        for(int i=1;i<=n;i++) s+=('0'+i);
        while(k-- >1)
            next_permutation(s.begin(),s.end());
        return s;
    }
};
