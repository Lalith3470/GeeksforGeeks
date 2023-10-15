
class Solution
{
public:
    int trailingZeroes(int N)
    {
        // Write Your Code here
        int count =0;
        while(N>=5){
            count+= N/5;
            N/=5;
        }
        return count ;
    }
};
